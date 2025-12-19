#!/bin/bash
# ATMOS CORE v3.0 - HEARTBEAT ALERT SENTINEL

WEBHOOK="PASTE_YOUR_DISCORD_WEBHOOK_URL_HERE"
THRESHOLD=1.05

echo "📡 Alert Sentinel Active. Monitoring HWM Variance..."

# Execute main.go and pipe its output to a loop for analysis
CGO_ENABLED=0 go run main.go | while read -r line; do
    echo "$line"
    # Extract the variance value from the Heartbeat line
    VARIANCE=$(echo "$line" | grep -oP 'Δ: \K[0-9.]+')
    
    if [ ! -z "$VARIANCE" ]; then
        if (( $(echo "$VARIANCE > $THRESHOLD" | bc -l) )); then
            NODE_ID=$(md5sum <<< "$(hostname)" | cut -c 1-8)
            TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
            
            echo -e "\e[1;31m🛑 HWM BREACH DETECTED: $VARIANCE\e[0m"
            
            # Send the Webhook Alert
            curl -s -X POST -H "Content-Type: application/json" \
                -d "{\"content\": \"🚨 **HWM BREACH ALERT**\n**Node ID:** \`$NODE_ID\`\n**Variance:** \`$VARIANCE\`\n**Time:** \`$TIMESTAMP\`\n**Status:** Network Instability Detected.\"}" \
                "$WEBHOOK" > /dev/null
        fi
    fi
done

