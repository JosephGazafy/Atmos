#!/bin/bash
# ATMOS CORE v3.0 - AUTOPILOT
chmod +x *.sh

./logo.sh
echo -e "\e[1;35m🚀 ENGAGING AUTOPILOT...\e[0m"

# Start the Watchdog in the background
./watchdog.sh > /dev/null 2>&1 &
echo "✅ Watchdog: ACTIVE"

# Start the Scuttle Timer in the background
./scuttle.sh > /dev/null 2>&1 &
echo "✅ Security Timer: ENGAGED"

# Handover to the Sentinel
./sovereign.sh mesh

