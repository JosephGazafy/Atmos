#!/bin/bash
# ATMOS CORE v3.0 - MASTER AUTOPILOT
chmod +x *.sh

./logo.sh
echo -e "\e[1;35m🚀 ENGAGING FULL-SPECTRUM AUTOPILOT...\e[0m"

# 1. Start Background Security
./watchdog.sh > /dev/null 2>&1 &
./scuttle.sh > /dev/null 2>&1 &

# 2. Start Acoustic Shield (Python)
python3 acoustic_shield.py > /dev/null 2>&1 &
echo "✅ Acoustic Shield: ACTIVE"

# 3. Launch Sentinel
echo "✅ US-East Anchor: 1.1.1.1"
./sovereign.sh mesh

# ... existing logic ...
# 4. Engage Lock Screen Dashboard
chmod +x mesh_notify.sh
./mesh_notify.sh
echo "✅ Lock Screen Dashboard: ENGAGED"

