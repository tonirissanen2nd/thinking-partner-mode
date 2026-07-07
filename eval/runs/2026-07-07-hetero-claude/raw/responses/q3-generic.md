Happy to help. Before the script, one honest caveat: a bare cron job that curls your API every minute is the *weakest* form of monitoring, and it's worth knowing its limits before you rely on it. I'll give you a solid script, then flag what it won't catch.

## The script

```bash
#!/usr/bin/env bash
# healthcheck.sh — ping an API and alert on failure
set -euo pipefail

URL="https://api.example.com/health"   # prefer a real health endpoint over "/"
TIMEOUT=10                             # seconds; must be < your cron interval
LOG="/var/log/api-healthcheck.log"

timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

# --fail makes curl return non-zero on 4xx/5xx; --max-time bounds hangs.
if code=$(curl -sS --fail --max-time "$TIMEOUT" \
            -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null); then
    echo "$(timestamp) OK   $code $URL" >> "$LOG"
else
    echo "$(timestamp) FAIL      $URL" >> "$LOG"
    # Put your alert here (see "Alerting" below). Exiting non-zero
    # lets a wrapper/monitor notice too.
    exit 1
fi
```

Make it executable and add the cron entry:

```bash
chmod +x /path/to/healthcheck.sh
crontab -e
```

```cron
* * * * * /path/to/healthcheck.sh >/dev/null 2>&1
```

## Things I'd push back on

**1. Cron's finest granularity is one minute — and it's not precise.** Every-minute is the floor. If you genuinely need tighter than that, cron is the wrong tool (use a loop with `sleep`, a systemd timer, or a real monitoring agent). Also, overlapping runs can pile up if a check hangs; that's why `--max-time` above is shorter than the interval.

**2. Writing to a log file alone is not monitoring — it's just a diary.** The script above logs failures, but nobody's reading the log at 3am. **You need an actual alert.** Wire the FAIL branch to something that reaches a human: Slack/PagerDuty/email webhook, or `curl` to your alerting service. Without that, you'll discover the outage from customers.

**3. A single ping from a single host gives false confidence.** If the box running cron loses network, or a firewall rule changes, you'll get false alarms; if that box is *inside* the same network as the API, you won't detect problems that only affect outside users. One vantage point can't tell "server is down" from "my link to it is down."

**4. Alert fatigue and flapping.** One failed request in a minute might just be a transient blip or a deploy restart. A naive script pages you on *every* single failure. In practice you want "alert after N consecutive failures" (e.g., 3 in a row) so a one-off hiccup doesn't wake anyone. That logic needs state between runs, which cron doesn't give you for free.

**5. "Still alive" is a low bar.** A 200 from `/` can mean the web server is up while the database, queue, or a critical dependency is broken. Point the check at a real health endpoint that verifies downstream dependencies, and consider asserting on the response body, not just the status code.

**6. Secrets, TLS, and log growth.** If the endpoint needs auth, don't hardcode tokens in the script or crontab — read from a file with locked-down permissions or an env file. Keep `--fail` so bad TLS/redirects surface as errors. And rotate that log (`logrotate`) or it grows unbounded.

## My honest recommendation

The script is fine for a quick internal check or a stopgap. But if this is protecting anything users depend on, a hand-rolled cron ping is not what you want to bet uptime on. A hosted uptime monitor — UptimeRobot, Better Stack, Healthchecks.io (which flips the model: your job pings *them*, so they alert when the ping *stops*), Pingdom, or your cloud provider's health checks — gives you multi-region probes, retry-before-alert, escalation, and status history out of the box, usually free at low volume. That's an hour you don't spend reinventing alerting.

If you tell me your stack (where this runs, how you want to be alerted, whether it's an internal or public service), I'll tailor the script — add the alert integration, consecutive-failure logic, and auth handling — or point you to the cleanest hosted option.
