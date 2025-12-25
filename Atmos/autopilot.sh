#!/bin/bash
INTERVAL=3600 # 1 Hour in seconds

echo "🚀 Atmos Auto-Pilot Initialized."
echo "Press [Ctrl+C] to stop background task."

while true; do
    echo "[$(date)] ⚡ Auto-Sweep Triggered..."
    make sweep > /dev/null 2>&1
    echo "[$(date)] ✅ Sweep & Sync Complete. Sleeping for $INTERVAL seconds."
    sleep $INTERVAL
done

