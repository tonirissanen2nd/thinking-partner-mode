Sure. Here's a straightforward version, plus a few things worth deciding before you wire it up.

```bash
#!/usr/bin/env bash
# /usr/local/bin/api-healthcheck.sh
set -uo pipefail

URL="${HEALTHCHECK_URL:-https://api.example.com/health}"
TIMEOUT=5           # seconds; must be well under your 60s interval
RETRIES=2           # quick retries before declaring a failure
STATE_FILE="/var/lib/api-healthcheck/state"
LOG="/var/log/api-healthcheck.log"

mkdir -p "$(dirname "$STATE_FILE")"

log() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$LOG"; }

check() {
  # -f: fail on HTTP >= 400, -s: silent, -S: still show errors
  curl -fsS --max-time "$TIMEOUT" --retry "$RETRIES" --retry-delay 1 \
       -o /dev/null -w '%{http_code} %{time_total}' "$URL"
}

if result="$(check 2>&1)"; then
  status="up"
  detail="$result"
else
  status="down"
  detail="$result"
fi

prev="$(cat "$STATE_FILE" 2>/dev/null || echo unknown)"
echo "$status" > "$STATE_FILE"

log "$status $detail"

# Only alert on transitions, so you don't get 1,440 pages a day.
if [ "$status" != "$prev" ]; then
  notify "API is now $status ($detail)"
fi
```

Where `notify` is whatever you actually use, e.g.:

```bash
notify() {
  curl -fsS -X POST "$SLACK_WEBHOOK_URL" \
    -H 'Content-Type: application/json' \
    -d "$(jq -nc --arg t "$1" '{text: $t}')" >/dev/null || true
}
```

Then:

```bash
chmod +x /usr/local/bin/api-healthcheck.sh
```

```cron
# m h dom mon dow  command
* * * * * SLACK_WEBHOOK_URL=... /usr/local/bin/api-healthcheck.sh
```

Or edit with `crontab -e`. Note cron gives you a minimal `PATH`, so use absolute paths (`/usr/bin/curl`) if anything can't be found.

Cron's floor is one minute. That's fine here, but it means you cannot go finer without a `sleep` loop inside the script (ugly) or a different scheduler.

Overlapping runs. If the API hangs, a 60-second cron can stack up processes. The `--max-time 5` above mostly prevents this, but `flock` makes it airtight:

```cron
* * * * * /usr/bin/flock -n /tmp/api-healthcheck.lock /usr/local/bin/api-healthcheck.sh
```

Alert on transitions, not on every failure. The state file above does this. Without it, a 20-minute outage means 20 identical alerts. You may also want to require N consecutive failures before alerting, to ride out blips.

A cron job on the same box as the API tells you nothing when the box dies — cron dies with it. If this check is meant to catch real outages, run it from a separate host, or use an external service (Healthchecks.io, UptimeRobot, Better Stack, or your cloud provider's synthetic monitor). A common middle ground is a dead-man's-switch: the cron job pings an external URL on success, and the external service alerts you if the ping stops arriving. That catches both "API is down" and "the whole machine is gone."

A `/health` endpoint that returns 200 unconditionally proves only that the process is listening. A more useful one checks the DB connection, the cache, and any critical downstream, and returns a non-200 when they're broken. Worth making sure the endpoint you're polling actually asserts something.

systemd timer alternative. If you're on systemd, a timer gives you better logging (`journalctl -u api-healthcheck`), built-in overlap protection, and randomized delay:

```ini
# /etc/systemd/system/api-healthcheck.service
[Unit]
Description=API health check

[Service]
Type=oneshot
Environment=SLACK_WEBHOOK_URL=...
ExecStart=/usr/local/bin/api-healthcheck.sh
```

```ini
# /etc/systemd/system/api-healthcheck.timer
[Unit]
Description=Run API health check every minute

[Timer]
OnCalendar=*:0/1
AccuracySec=1s

[Install]
WantedBy=timers.target
```

```bash
systemctl enable --now api-healthcheck.timer
```

Happy to adapt this — if you tell me where it'll run, what "down" should trigger, and whether you already have a monitoring stack, I can tighten it up.
