#!/bin/bash
# ATMOS CORE v3.0 - PERSISTENT WATCHDOG

echo "🛡️ Watchdog Daemon Started. Monitoring Kill Switch..."

while true; do
    # Run the Kill Switch check
    ./killswitch.sh
    
    # Check if the Sentinel is still running, restart if it crashed
    if ! pgrep -f "alert_sentinel.sh" > /dev/null; then
        echo "⚠️ Sentinel dropped. Restarting..."
        ./alert_sentinel.sh &
    fi
    
    # Sleep for 300 seconds (5 minutes)
    sleep 300
done

