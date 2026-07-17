# Question

I want to set up a cron job that pings our API every minute to check if the server is still alive — can you help me write the script?

---

# Answer 1

Absolutely! Here's a straightforward way to set up a cron job that pings your API every minute.

First, create a monitoring script (e.g., `monitor_api.sh`):

```bash
#!/bin/bash

API_URL="https://your-api.com/health"  # Change this to your API endpoint
LOG_FILE="/var/log/api_monitor.log"
TIMEOUT=5

# Make the request and check status
if curl -s --max-time $TIMEOUT "$API_URL" > /dev/null 2>&1; then
    echo "$(date): API is UP" >> $LOG_FILE
else
    echo "$(date): API is DOWN - $(date)" >> $LOG_FILE
    # Optional: Send alert (email, Slack, etc.)
    # Example: mail -s "API Down Alert" admin@example.com < $LOG_FILE
fi
```

Make it executable:
```bash
chmod +x /path/to/monitor_api.sh
```

Edit your crontab:
```bash
crontab -e
```

Add this line to run every minute:
```bash
* * * * * /path/to/monitor_api.sh
```

If you want to add alerts when the API goes down:

```bash
#!/bin/bash

API_URL="https://your-api.com/health"
LOG_FILE="/var/log/api_monitor.log"
STATUS_FILE="/tmp/api_status"
TIMEOUT=5

if curl -s --max-time $TIMEOUT "$API_URL" > /dev/null 2>&1; then
    echo "UP" > $STATUS_FILE
    echo "$(date): API is UP" >> $LOG_FILE
else
    # Check if we just transitioned from UP to DOWN
    if [ -f $STATUS_FILE ] && [ "$(cat $STATUS_FILE)" = "UP" ]; then
        echo "DOWN" > $STATUS_FILE
        echo "$(date): API DOWN ALERT" >> $LOG_FILE
        # Send alert
        curl -X POST https://hooks.slack.com/services/YOUR/WEBHOOK/URL \
             -d '{"text":"API is DOWN"}'
    fi
fi
```

- Use absolute paths in cron jobs (not relative paths)
- Redirect output to a log file to track history
- Use `--max-time` with curl to avoid hanging
- Consider using a lightweight health check endpoint if available
- For critical APIs, add alerting via Slack, email, or PagerDuty
- Test the script manually before adding to cron: `bash /path/to/monitor_api.sh`

Let me know if you need help customizing this for your specific API or adding additional alerting!

---

# Answer 2

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
