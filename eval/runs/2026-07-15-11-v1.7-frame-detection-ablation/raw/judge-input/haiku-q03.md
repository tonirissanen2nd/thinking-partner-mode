# Question

I want to set up a cron job that pings our API every minute to check if the server is still alive — can you help me write the script?

---

# Answer 1

Yes, though the approach has limits. Here's a working baseline:

```bash
#!/bin/bash
API_URL="https://your-api.com/health"
LOG_FILE="/var/log/api-ping.log"
TIMEOUT=5

response=$(curl -s -o /dev/null -w "%{http_code}" --max-time $TIMEOUT "$API_URL")
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

if [ "$response" = "200" ]; then
  echo "[$timestamp] OK (HTTP $response)" >> "$LOG_FILE"
else
  echo "[$timestamp] FAIL (HTTP $response)" >> "$LOG_FILE"
fi
```

Add to crontab with `crontab -e`:
```
* * * * * /path/to/script.sh
```

This works only if you clarify first:
- What endpoint and what HTTP status code means "alive"? (Assume 200 here; adjust as needed.)
- Which OS? (Linux/macOS: cron works as shown. Windows: use Task Scheduler or WSL.)
- Should transient network failures trigger an alert, or just log them? (Script above logs silently; you'll need external logic to alert.)
- How long can a response take before the server counts as "down"? (5-second timeout above; adjust `TIMEOUT` if needed.)

A single cron job that pings is brittle—it conflates monitoring infrastructure with health checking. If this is production:
- Use a dedicated monitoring tool (Prometheus, Datadog, New Relic, Uptime Robot) instead. These handle alerting, dashboarding, and incident triage automatically.
- A cron job cannot distinguish a transient glitch (flaky network, 1-second spike) from real failure. Proper monitoring applies thresholds (alert only after 2–3 consecutive failures) and temporal context.
- Logs in a file become noise without a log aggregator (ELK, Splunk, CloudWatch) to alert on patterns.

This is a development environment, a low-stakes check, or a temporary bandage until real monitoring is in place. Otherwise, the upfront cost of a monitoring service pays back in signal-to-noise.

---

# Answer 2

Yes, I can help. Here's a basic script and cron setup:

```bash
#!/bin/bash
curl -f -m 5 https://your-api.com/health || echo "API down at $(date)" >> /var/log/api-health.log
```

Add to crontab: `* * * * * /path/to/script.sh`

This pings your API every minute with a 5-second timeout, and logs failures.

Pinging without alerting is incomplete. If the API goes down, your log fills with records, but no one acts on it unless they're actively watching. That defeats the health-check purpose.

Replace passive logging with active alerting. At minimum:
- Send alerts (Slack, email, PagerDuty) on first failure
- Add exponential backoff (don't spam after confirmed downtime)
- Log successes and failures separately
- Check the HTTP response code, not just connection
- Set a reasonable timeout per your latency tolerance

A basic example with exit-on-success alerting:
```bash
#!/bin/bash
HEALTH_URL="https://your-api.com/health"
RESPONSE=$(curl -s -w "%{http_code}" -m 5 "$HEALTH_URL" -o /tmp/health.out 2>&1)
CODE=${RESPONSE: -3}
if [[ "$CODE" != "200" ]]; then
  echo "API unhealthy ($CODE) at $(date)" >> /var/log/api-failures.log
  # Add your alert here (curl to Slack webhook, mail command, etc.)
else
  # Optional: log success occasionally to confirm monitoring works
  echo "API healthy at $(date)" >> /var/log/api-success.log
fi
```

Without seeing your API's response characteristics (typical latency, failure modes, SLA), I can't calibrate the timeout or backoff strategy precisely. Adjust the 5-second timeout based on your P99 latency.

If you're doing this for production observability, consider using a proper monitoring system (Prometheus, Datadog, New Relic) instead of a cron-based check. A dedicated system handles alerting, aggregation, and escalation better than a shell script, and won't silently fail if cron itself crashes or the server reboots.
