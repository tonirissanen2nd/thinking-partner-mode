Here's a working script. Then one structural issue worth more of your attention than the script itself.

```bash
#!/usr/bin/env bash
# healthcheck.sh — ping API, alert on failure
set -uo pipefail

URL="https://api.example.com/health"   # prefer a real health endpoint over any old route
TIMEOUT=10                              # seconds; must be < cron interval
STATE_FILE="/var/tmp/api_health.state"  # tracks last known state to avoid alert spam

# --connect-timeout guards against a hung TCP connect; --max-time bounds the whole request.
code=$(curl -sS -o /dev/null -w '%{http_code}' \
  --connect-timeout 5 --max-time "$TIMEOUT" "$URL" 2>/dev/null) || code="000"

prev=$(cat "$STATE_FILE" 2>/dev/null || echo "up")

if [[ "$code" == "200" ]]; then
  if [[ "$prev" != "up" ]]; then
    logger -t healthcheck "API recovered (HTTP $code)"
    # send-recovery-notification here
    echo "up" > "$STATE_FILE"
  fi
else
  logger -t healthcheck "API DOWN (HTTP $code)"
  if [[ "$prev" != "down" ]]; then
    # send-alert here (email / PagerDuty / Slack webhook)
    echo "down" > "$STATE_FILE"
  fi
fi
```

Crontab entry:

```
* * * * * /path/to/healthcheck.sh
```

Design choices that matter, since they're easy to get wrong:

- Timeout shorter than the interval. With a 1-minute cron and no `--max-time`, a hung request can leave overlapping invocations piling up. Bound it well under 60s.
- Edge-triggered alerting via the state file. Without it, a 3-hour outage sends ~180 identical alerts and you learn to ignore the channel. Alert on the *transition* down and on recovery, not on every failing poll. (You may want the opposite for a few consecutive failures before firing — see flapping below.)
- `%{http_code}` not exit status. `curl` exits 0 on a 500. Check the actual code; treat a connection failure as `000`.
- Treat a single failure with suspicion. One dropped packet shouldn't page anyone. A common refinement is "N consecutive failures" before declaring down — worth adding if the endpoint is even slightly flaky.

If this cron job runs *on the same server whose liveness you're checking*, it cannot do the job you want. The failure modes that actually take an API down — kernel panic, OOM, the box losing power or network, the host disappearing — also take down the cron daemon running the check. In exactly the case you most need to hear about, the checker is dead too and stays silent. A monitor co-located with the thing it monitors has a blind spot precisely over total failure, which is usually the failure that matters most. (This is a definitional property of co-location, not an empirical claim about your setup.)

So the check is only as good as its vantage point:

- Off-box is the real fix. Run the check from a *different* machine, or use an external uptime service (healthchecks.io, UptimeRobot, Better Stack, a Pingdom-class tool, or a probe from your cloud provider's monitoring). External probing is the standard answer to "is my server alive," and it's what I'd reach for over a self-hosted cron unless you have a specific reason not to.
- Dead-man's-switch pattern. Invert it: your server periodically pings an external service, and *that service* alerts when the ping stops arriving. This survives your box vanishing entirely, which the pull-based script above does not. healthchecks.io is built specifically around this pattern.
- If it must be self-hosted, put the checker on a separate host in a different failure domain (ideally different power/network) from the API.

The script is genuinely useful for a narrower question — "is the API process returning errors or hanging while the box is otherwise up" — e.g. run from a monitoring host against your fleet. That's a real use. It's just not the same question as "is the server still alive," and conflating the two is how outages go unnoticed.

One thing I haven't addressed because you didn't specify it: what should *happen* on failure (page a human, auto-restart, failover). The alerting stub above is a placeholder; the right action depends on whether this is production infrastructure or a side project, which changes the answer materially. Happy to fill that in if you tell me the context.
