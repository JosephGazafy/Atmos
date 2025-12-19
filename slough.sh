#!/bin/bash
# ATMOS CORE v3.0 - EMERGENCY SHADOW-WIPE
./logo.sh
echo -e "\e[1;31m🔥 INITIATING TOTAL DATA RELINQUISHMENT...\e[0m"

# 1. Kill all background daemons
pkill -f "watchdog.sh"
pkill -f "scuttle.sh"
pkill -f "alert_sentinel.sh"

# 2. Shred temporary files and logs
rm -rf $TMPDIR/*
rm -f ~/.bash_history
rm -f ~/Atmos/*.log
touch ~/.bash_history

# 3. Lock the vault
chmod 000 ~/Atmos/.atmos_vault*

echo -e "\e[1;32m✅ SESSION SHREDDED. TRACES REMOVED.\e[0m"
exit 0

