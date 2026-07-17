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

Yes. Here's a working version, then the failure mode that matters more than the script.

Assuming Linux + bash, a health endpoint that returns 200, and somewhere to send an alert (Slack webhook below; swap for whatever you use).

`/usr/local/bin/api-healthcheck.sh`:

```bash
#!/usr/bin/env bash
set -uo pipefail

URL="https://api.example.com/healthz"
TIMEOUT=5
FAIL_THRESHOLD=3                 # consecutive failures before alerting
WEBHOOK="${SLACK_WEBHOOK_URL:?set SLACK_WEBHOOK_URL}"
STATE_FILE=/var/lib/api-healthcheck/consecutive_failures

mkdir -p "$(dirname "$STATE_FILE")"
[ -f "$STATE_FILE" ] || echo 0 > "$STATE_FILE"
fails=$(cat "$STATE_FILE")

notify() {
  curl -sS --max-time 10 -X POST -H 'Content-Type: application/json' \
    -d "{\"text\":\"$1\"}" "$WEBHOOK" >/dev/null
}

code=$(curl -sS -o /dev/null -w '%{http_code}' --max-time "$TIMEOUT" "$URL") || code=000

if [ "$code" = "200" ]; then
  if [ "$fails" -ge "$FAIL_THRESHOLD" ]; then
    notify "RECOVERED: $URL healthy after $fails failed checks"
  fi
  echo 0 > "$STATE_FILE"
  exit 0
fi

fails=$(( fails + 1 ))
echo "$fails" > "$STATE_FILE"

# -eq, not -ge: fire once on crossing the threshold, not every minute for an hour
if [ "$fails" -eq "$FAIL_THRESHOLD" ]; then
  notify "DOWN: $URL returned '$code' on $fails consecutive checks"
fi
```

Crontab:

```
* * * * * /usr/bin/flock -n /var/lock/api-healthcheck.lock /usr/local/bin/api-healthcheck.sh >> /var/log/api-healthcheck.log 2>&1
```

Three things in there that a naive version omits and that you want regardless of what you do next: `--max-time` (an unbounded curl against a hung server stacks up processes forever), `flock -n` (skip the run rather than overlap it), and the consecutive-failure counter (one dropped packet should not page you, and a real outage should page you once, not sixty times an hour).

Note: `flock` is util-linux, so Linux only — on macOS it isn't present by default and you'd use launchd instead of cron anyway. (If you're on macOS, verify before relying on the cron line.)

If this cron runs on the API host, it cannot detect the failures you most need to detect.

Host kernel panics, instance gets terminated, network interface drops, disk fills up so cron can't fork — in every one of those cases the checker dies with the thing it's checking, and you get no alert. Silence from this system is indistinguishable from health. That's not a bug you can patch in the script; it's structural, and it's the standard way homegrown monitoring fails silently for months and then fails to fire on the one outage it existed for.

Two fixes, in order of preference:

1. Run the check from somewhere else. If you have a second box, put the cron there — you now also cover the network path, which is a real fraction of "the API is down" incidents. If you don't, use an external uptime monitor (UptimeRobot, Better Stack, Pingdom, or blackbox_exporter + Alertmanager if you already run Prometheus). You get off-host checking, multi-region confirmation to kill false positives, alert dedup and escalation, and outage history — all things this script would take you months of accreted patches to approximate badly. (Pricing pages move; check before committing.)
2. Add a dead man's switch. Whatever runs the check, have it ping a heartbeat endpoint (healthchecks.io, Cronitor, Dead Man's Snitch) after each successful run, configured to alert if the ping stops. This inverts the failure mode: absence of signal becomes an alarm rather than a silence. If you keep the on-host cron, this is the minimum viable correction, and it's a two-line change.

HTTP 200 is a liveness check, not a health check. A process that's up but has an exhausted DB connection pool, a full disk, or a 90-second queue backlog will happily return 200 while the product is unusable. If `/healthz` just returns a static string, you're monitoring "did nginx start." Give it a shallow dependency check — DB ping, cache ping, with its own short timeout so the health endpoint can't itself hang.

Every-minute polling plus a 3-failure threshold means ~3 minutes minimum to detect. If your target is tighter than that, cron can't help — 1 minute is its floor — and you'd move to a systemd timer with `OnUnitActiveSec`, or an external monitor polling at 30s/10s.

Authentication on the health endpoint (if it's public and does a DB query, it's a cheap DoS lever and a status leak); where alerts route when the person who owns that webhook is asleep; rotation of that log file; and TLS certificate expiry, which is a common outage cause that a 200-check only notices at the moment it has already broken you — worth a separate check with a 14-day warning.

The API is on a private network no external monitor can reach and you have no monitoring stack to hang this off. In that case keep the script, move it to a different host inside the network, and add the heartbeat. Otherwise the external monitor is strictly less work than maintaining this.
