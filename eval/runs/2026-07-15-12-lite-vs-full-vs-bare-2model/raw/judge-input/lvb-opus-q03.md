# Question

I want to set up a cron job that pings our API every minute to check if the server is still alive — can you help me write the script?

---

# Answer 1

Happy to help with the script. One thing worth flagging first, since it affects how you'll want to build this: a cron job that pings your API every minute is a fine *heartbeat* check, but it's a fairly weak *alerting* setup on its own. Cron will run your script; it won't tell you when the script itself notices the server is down, unless you add that part. So the real work is less "write the ping" and more "decide what happens on failure and how you get told." I'll give you the ping and wire in a place for that.

Here's a straightforward Bash version:

```bash
#!/usr/bin/env bash
# healthcheck.sh — ping API, alert on failure

URL="https://your-api.example.com/health"   # use a real health endpoint if you have one
TIMEOUT=10                                    # seconds; must be < 60 so it can't overlap the next run

# -f: fail on HTTP >= 400; -s: silent; -S: still show errors; -o /dev/null: discard body
if curl -fsS --max-time "$TIMEOUT" -o /dev/null "$URL"; then
    exit 0
else
    # This is where alerting goes. Options below.
    echo "$(date -u +%FT%TZ) health check FAILED for $URL" >> /var/log/healthcheck.log
    # e.g. send to a webhook / paging service here
    exit 1
fi
```

Crontab entry (`crontab -e`):

```
* * * * * /path/to/healthcheck.sh
```

A few things I'd decide before trusting this, roughly in order of how much they matter:

- How you actually get alerted. Logging to a file means nobody finds out until they read the file. If the point is to know the server died, you need the failure branch to *notify* you — a webhook to Slack/Discord, a call to a paging service, or an email via a service that won't itself be down when your box is. I left a placeholder rather than guessing your stack; tell me what you use and I'll fill it in.

- What "alive" means. A plain ping to `/` tells you the port answers. A dedicated `/health` endpoint that checks the DB, dependencies, etc., tells you the app actually works. Prefer the latter if you have one; if you don't, that's often more valuable to build than the cron script.

- Flapping. One failed ping out of a minute could be a transient blip. Many people only alert after N consecutive failures to avoid noise. Worth adding a small counter/state file if you find yourself getting paged for nothing.

- Timeout discipline. I set --max-time 10 so a hung request can't run long enough to overlap the next minute's run. Without a timeout, cron will happily stack up processes against a slow server.

- The blind spot cron can't cover: if the whole machine (or cron itself) goes down, nothing runs and you get silence, not an alert — which reads exactly like "everything's fine." For real production monitoring, an external service (UptimeRobot, Healthchecks.io, a cloud monitor, etc.) pinging *from outside* your infrastructure closes that gap. A self-hosted cron check is a good complement to that, not really a replacement.

That last point is the one I'd push on: if this is protecting something you care about, monitoring the server from the same server has a fundamental hole in it. If it's just a quick internal sanity check, the script above is plenty.

Want me to wire in a specific alert channel, or convert this to a systemd timer (slightly more robust than cron for this) or PowerShell if you're on Windows?

---

# Answer 2

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
