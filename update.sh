#!/bin/bash
# ATMOS CORE v3.0 - SECURE UPDATE & AUTO-REGISTRY
./logo.sh
echo -e "\e[1;33m🔄 INITIATING MANIFEST SYNC...\e[0m"

FILES=("sovereign.sh" "logo.sh" "main.go" "sovereign_init.py" "slough.sh" "welcome.txt" "registry.sh" "update.sh" "autopilot.sh" "status.sh" "killswitch.sh" "watchdog.sh" "alert_sentinel.sh" "invite.sh")

for file in "${FILES[@]}"; do
    echo -n "📡 Syncing $file... "
    curl -s -LO "https://raw.githubusercontent.com/JosephGazafy/Atmos/main/$file"
    echo -e "\e[1;32m[DONE]\e[0m"
done

chmod +x *.sh

# Perform the Registry Handshake
./registry.sh

if [ -f "welcome.txt" ]; then
    cat welcome.txt
fi

echo -e "\e[1;32m✅ NODE FULLY SYNCHRONIZED AND REGISTERED.\e[0m"

