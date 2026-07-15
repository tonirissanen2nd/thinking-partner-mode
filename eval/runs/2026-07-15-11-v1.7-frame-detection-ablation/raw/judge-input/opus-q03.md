# Question

I want to set up a cron job that pings our API every minute to check if the server is still alive — can you help me write the script?

---

# Answer 1

Yes — but before the script, one structural point about the goal, because the naive version of this monitor will mislead you in exactly the situation you're building it for.

A cron job on your own server that pings your own API tells you almost nothing about whether the server is "still alive." If the box hangs, loses network, runs out of memory, or the cron daemon itself dies, the check dies with it — silently. You get no alert precisely when the thing you're watching is down. This is the classic flaw of self-hosted liveness checks: the monitor shares a fate with the monitored. For real liveness detection you want the check to run *off* the machine (an external uptime service, a separate host, or a dead-man's-switch pattern where silence itself triggers the alert).

I'll give you both: the local script you asked for (useful for logging and for a self-contained restart-on-failure loop), and the pointer to the off-box version, since that's the one that actually does what "check if the server is still alive" implies.

Local script (`healthcheck.sh`):

```bash
#!/usr/bin/env bash
set -uo pipefail

URL="https://your-api.example.com/health"   # use a real health endpoint, not "/"
TIMEOUT=10                                    # seconds; must be < your cron interval
LOG="/var/log/api-healthcheck.log"

code=$(curl -sS -o /dev/null -w '%{http_code}' \
       --max-time "$TIMEOUT" "$URL" 2>>"$LOG")

ts=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
if [[ "$code" == "200" ]]; then
  echo "$ts OK $code" >> "$LOG"
else
  echo "$ts FAIL $code" >> "$LOG"
  # alerting hook goes here — see note below
fi
```

Crontab entry (every minute):

```
* * * * * /path/to/healthcheck.sh
```

A few things worth flagging, in rough order of how likely each is to bite you:

- Cron's minimum resolution is one minute. If you genuinely need sub-minute checks, cron is the wrong tool — use a `systemd` timer, a small daemon with a sleep loop, or an external monitor. As written, `* * * * *` is the finest cron will do.
- `--max-time` must be shorter than the interval. With a 1-minute cron and no timeout, a hung connection lets checks pile up on top of each other. The `TIMEOUT=10` above prevents that; don't remove it.
- Check a real health endpoint, not `/`. Pinging `/` often returns 200 from a front proxy even when the app behind it is dead. A `/health` route that touches the DB/dependencies and returns 200 only when the app can actually serve is far more meaningful. (This is the difference between "the port answers" and "the service works" — decide which one you actually mean by "alive.")
- The `echo`-only failure branch does nothing but log. Logging that a server is down, on the server that is down, to a disk you may not be able to read, is not an alert. You need the failure branch to reach *outward* — a webhook to Slack/PagerDuty/healthchecks.io, an email via an external relay, etc. I left it as a comment rather than guess your stack; tell me what you use and I'll fill it in.
- Watch for flapping. One failed request on a 1-minute cadence will fire an alert on a transient blip. If you add alerting, gate it on N consecutive failures (e.g., track a counter in a state file) so you're not paged for every dropped packet.

What I'd actually recommend as primary: point an external service at your `/health` endpoint (healthchecks.io, UptimeRobot, Better Stack, a Pingdom-class tool, or a cron job on a *different* machine). Or invert it into a dead-man's-switch: your server pings the external service every minute, and *that* service alerts you when the pings stop. Either way the alerting path doesn't die when the server does. Keep the local script for logging and for driving an automatic restart (e.g., feeding a `systemd` unit's `Restart=on-failure`), but don't let it be your only line of sight.

It's a well-established failure mode, not a judgment call. The cron-resolution and timeout points are standard behavior. What I don't know: your interval requirements, your alerting stack, and whether you already have external monitoring and just wanted the local piece — if the last is true, ignore the framing critique and the script above is ready to go once you set `URL` and the alert hook.

---

# Answer 2

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
