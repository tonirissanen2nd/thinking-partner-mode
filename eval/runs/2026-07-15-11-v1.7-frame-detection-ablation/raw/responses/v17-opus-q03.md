Yes — but before the script, one structural point about the goal, because the naive version of this monitor will mislead you in exactly the situation you're building it for.

**The trap:** a cron job on your own server that pings your own API tells you almost nothing about whether the server is "still alive." If the box hangs, loses network, runs out of memory, or the cron daemon itself dies, the check dies with it — silently. You get no alert precisely when the thing you're watching is down. This is the classic flaw of self-hosted liveness checks: the monitor shares a fate with the monitored. For real liveness detection you want the check to run *off* the machine (an external uptime service, a separate host, or a dead-man's-switch pattern where silence itself triggers the alert).

I'll give you both: the local script you asked for (useful for logging and for a self-contained restart-on-failure loop), and the pointer to the off-box version, since that's the one that actually does what "check if the server is still alive" implies.

**Local script** (`healthcheck.sh`):

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

- **Cron's minimum resolution is one minute.** If you genuinely need sub-minute checks, cron is the wrong tool — use a `systemd` timer, a small daemon with a sleep loop, or an external monitor. As written, `* * * * *` is the finest cron will do.
- **`--max-time` must be shorter than the interval.** With a 1-minute cron and no timeout, a hung connection lets checks pile up on top of each other. The `TIMEOUT=10` above prevents that; don't remove it.
- **Check a real health endpoint, not `/`.** Pinging `/` often returns 200 from a front proxy even when the app behind it is dead. A `/health` route that touches the DB/dependencies and returns 200 only when the app can actually serve is far more meaningful. (This is the difference between "the port answers" and "the service works" — decide which one you actually mean by "alive.")
- **The `echo`-only failure branch does nothing but log.** Logging that a server is down, on the server that is down, to a disk you may not be able to read, is not an alert. You need the failure branch to reach *outward* — a webhook to Slack/PagerDuty/healthchecks.io, an email via an external relay, etc. I left it as a comment rather than guess your stack; tell me what you use and I'll fill it in.
- **Watch for flapping.** One failed request on a 1-minute cadence will fire an alert on a transient blip. If you add alerting, gate it on N consecutive failures (e.g., track a counter in a state file) so you're not paged for every dropped packet.

**The off-box version**, which is what I'd actually recommend as primary: point an external service at your `/health` endpoint (healthchecks.io, UptimeRobot, Better Stack, a Pingdom-class tool, or a cron job on a *different* machine). Or invert it into a dead-man's-switch: your server pings the external service every minute, and *that* service alerts you when the pings stop. Either way the alerting path doesn't die when the server does. Keep the local script for logging and for driving an automatic restart (e.g., feeding a `systemd` unit's `Restart=on-failure`), but don't let it be your only line of sight.

Confidence that the self-monitoring gap is the real issue here: high — it's a well-established failure mode, not a judgment call. The cron-resolution and timeout points are standard behavior. What I don't know: your interval requirements, your alerting stack, and whether you already have external monitoring and just wanted the local piece — if the last is true, ignore the framing critique and the script above is ready to go once you set `URL` and the alert hook.
