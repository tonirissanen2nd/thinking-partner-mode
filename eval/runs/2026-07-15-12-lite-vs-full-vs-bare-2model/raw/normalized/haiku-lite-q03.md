Sure. Here's a basic setup:

Script (`check-api.sh`):
```bash
#!/bin/bash
API_URL="https://your-api.com/health"
LOG_FILE="/var/log/api-check.log"

response=$(curl -s -w "\n%{http_code}" -m 5 "$API_URL")
http_code=$(echo "$response" | tail -n1)
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

if [ "$http_code" -eq 200 ]; then
    echo "[$timestamp] OK - HTTP $http_code" >> "$LOG_FILE"
else
    echo "[$timestamp] ALERT - HTTP $http_code" >> "$LOG_FILE"
    # Optional: send alert (email, Slack, PagerDuty, etc.)
fi
```

Cron entry (run `crontab -e`):
```
* * * * * /path/to/check-api.sh
```

- Timeout: The `-m 5` flag times out after 5 seconds. Adjust if needed.
- Alerting: The script logs failures but doesn't alert yet. Add email (`mail`), Slack webhook, or another service if you want notifications.
- Log rotation: Without rotation, `/var/log/api-check.log` will grow indefinitely. Use `logrotate` or truncate periodically.
- False positives: One failed request might be transient. Consider requiring 2-3 consecutive failures before alerting.
- Permissions: The cron user needs write access to the log directory. Run `chmod 755 /path/to/check-api.sh` and ensure the log directory exists.

Make the script executable: `chmod +x /path/to/check-api.sh`

That's a solid foundation. What's your alert strategy — logging only, or do you need active notifications?
