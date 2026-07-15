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
