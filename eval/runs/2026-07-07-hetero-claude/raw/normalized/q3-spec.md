Happy to — but the means you've picked has a structural flaw worth fixing before I hand you a script, because the script is the easy part.

A cron job checking whether the server is alive, running *on that same server*, can't do the one thing you want. If the box goes down — kernel panic, OOM, power, network partition — cron goes down with it, and you get silence, not an alert. Silence is indistinguishable from "everything's fine." This is the core issue — it's definitional, not empirical.

The second issue: a check that only *checks* isn't monitoring. If the ping fails at 3am and nothing routes that failure to a human or a pager, you've logged an outage, not detected one. "Ping the API" is the easy 20%; "decide it's really down and wake someone" is the 80%.

The better way, roughly in order of effort vs. payoff:

1. **External uptime monitor** — UptimeRobot, Betterstack, Pingdom, or a Healthchecks.io "dead man's switch," plus a cloud provider's health check if you're already on AWS/GCP/etc. These run off your infrastructure, so they survive your server dying, and they handle alerting, retries, and escalation for you. For plain "is it up," this is almost certainly what you actually want, and most have usable free tiers. I don't know your constraints, though, so this may not fit — see below.

2. **Self-hosted from a *different* host** — if you can't use a third party (air-gapped, compliance, cost), run the check from a separate machine/region so the monitor and the target don't share a failure domain.

3. **Cron on the same box** — genuinely useful, but for a *different* job than the one you asked for: local resource/self-healing checks ("is my own disk full," "restart the worker if it died"), where being co-located is the point. Not for external liveness.

The one thing I'd steer you away from regardless of choice: hand-rolled every-minute cron as your *primary* external alerting. It reinvents retries, flap-suppression, and escalation — all of which the tools in (1) already solved.

What would change this: if you tell me you're on an air-gapped network, or already have a monitoring stack (Prometheus/Grafana, Datadog, Nagios) — then the answer shifts to "add a probe to what you have" and I'd point you there instead.

If you've weighed that and still want the same-host cron — reasonable as a *stopgap* or a supplement — here's a version that at least alerts instead of failing silently, and doesn't overlap on slow responses:

```bash
#!/usr/bin/env bash
# /usr/local/bin/ping-api.sh
set -euo pipefail

URL="https://api.example.com/health"   # use a real health endpoint, not "/"
TIMEOUT=10                             # seconds; must be < your cron interval
STATE_FILE="/var/tmp/api-health.state" # tracks up/down to alert on transitions

notify() {                             # replace with your real alert channel
  # e.g. curl to a Slack/PagerDuty webhook, or `mail`
  echo "$1" | logger -t ping-api
}

if curl --fail --silent --show-error --max-time "$TIMEOUT" "$URL" >/dev/null 2>&1; then
  status="up"
else
  status="down"
fi

last="$(cat "$STATE_FILE" 2>/dev/null || echo up)"
if [[ "$status" != "$last" ]]; then    # only alert on state change, not every minute
  notify "API health changed: $last -> $status ($URL)"
fi
echo "$status" > "$STATE_FILE"
```

Crontab entry:

```
* * * * * /usr/local/bin/ping-api.sh
```

Notes that matter:
- **Point `URL` at a real health endpoint** that touches your critical dependencies (DB, cache), not the homepage — otherwise you're testing that nginx serves bytes, not that the service works.
- **`--max-time` must be shorter than the interval** (here 10s < 60s) or slow responses stack up cron runs. If you need finer than one minute, cron can't do sub-minute granularity — you'd loop with `sleep` under a systemd service instead, which is also a cleaner home for this than crontab.
- **The state file** is what turns "silently failing check" into "alert on the transition." Without alerting wired into `notify()`, this script is still just logging — swap in your real channel (webhook/pager/email) or it doesn't do the job.

I don't know what you mean by "alive." A TCP/HTTP 200 tells you the process is listening; it doesn't tell you the API is *serving correctly* (returning good data, not throwing on every real request). If you care about the latter, the health endpoint needs to exercise the real path, and that's a design choice on the server side, not the cron side.

Tell me your environment (cloud provider, existing monitoring, any air-gap constraints) and I'll give you the specific setup rather than the generic one.
