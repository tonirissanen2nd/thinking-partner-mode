I can help with that. Here's a working cron job that pings your API every minute:

```bash
* * * * * /usr/bin/curl -s https://your-api.example.com/health || echo "API down at $(date)" >> /var/log/api-health.log
```

Add this to your crontab with `crontab -e`. This runs curl every minute; if the request fails, it logs the downtime. For better control:

```bash
* * * * * /path/to/check-api.sh
```

Where `check-api.sh` contains:
```bash
#!/bin/bash
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" https://your-api.example.com/health)
if [ "$RESPONSE" -ne 200 ]; then
  echo "API unhealthy: HTTP $RESPONSE at $(date)" >> /var/log/api-health.log
  # Optional: send alert, restart service, etc.
fi
```

**The suboptimal part:** A cron job pinging every 60 seconds has real limitations that matter in practice:

1. **Latency to detection** (Moderate confidence). Cron is not guaranteed to fire exactly at 60-second intervals; on loaded systems, the gap can be 2-3+ seconds. More significantly, if your API fails at second 30 of the minute, you won't detect it until second 60-90. For a monitoring service that's often unacceptable.

2. **No alerting chain** (High confidence). This logs failures but doesn't *alert* anyone or take corrective action. If no one checks the log, downtime goes unnoticed. You'd need a separate log-tail process watching for new entries.

3. **False positives and timeouts** (Moderate confidence). A single slow request failure can trigger an alert; timeouts aren't handled explicitly. If your API occasionally takes 30 seconds to respond, the curl default timeout will kill it and log a false positive.

4. **No context on what "alive" means** (High confidence). HTTP 200 is only one health indicator. A 503 response or connection timeout both fail the curl, but they mean different things operationally. Better monitoring tests specific endpoints and checks app logic health, not just network reachability.

**Better approach:** Use a proper monitoring agent (Prometheus + Alertmanager, Datadog, New Relic, or even a simpler tool like Uptime Kuma). These offer sub-minute detection windows, alerting, dashboards, and multi-layer health checks. If you cannot install external tooling, a cron job is workable *if* you add the missing pieces: explicit timeout handling, alert routing, and health-check specificity.

The cron solution above is correct for what you asked; use it if constraints require it. But if you have latitude, identify what you're actually trying to prevent (service downtime, customer impact, cascading failures), and design your monitoring around that outcome rather than around the lowest-friction implementation.

