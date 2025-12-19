#!/bin/bash
# ATMOS CORE v3.0 - SECURE UPDATE PROTOCOL
./logo.sh
echo -e "\e[1;33m🔄 INITIATING MANIFEST SYNC...\e[0m"

# Define the Master manifest
FILES=("sovereign.sh" "logo.sh" "main.go" "sovereign_init.py" "slough.sh" "welcome.txt" "registry.sh" "update.sh" "autopilot.sh" "status.sh" "killswitch.sh" "watchdog.sh" "alert_sentinel.sh")

# Pull each file from your GitHub Master Anchor
for file in "${FILES[@]}"; do
    echo -n "📡 Syncing $file... "
    curl -s -LO "https://raw.githubusercontent.com/JosephGazafy/Atmos/main/$file"
    if [ $? -eq 0 ]; then
        echo -e "\e[1;32m[DONE]\e[0m"
    else
        echo -e "\e[1;31m[FAILED]\e[0m"
    fi
done

chmod +x *.sh
echo "----------------------------------------------------"
echo -e "\e[1;32m✅ MANIFEST FULLY SYNCHRONIZED.\e[0m"

