#!/bin/bash
# ATMOS CORE v3.0 - LOGGING P2P TUNNEL
./logo.sh

VAULT=".atmos_vault"
SEED="origin-anchor-Judah-Joseph-180-phase-deciduous-stride-equitable-coefficient-archetypal-mesh-vivus-philo-navi-ping"

echo -e "\e[1;35m🔐 SECURE TUNNEL & VAULT ACTIVE\e[0m"
echo "----------------------------------------------------"
echo "1) Encrypt & Log Message"
echo "2) Decrypt String"
echo "3) View Encrypted Vault"
read -p "Selection: " CHOICE

case "$CHOICE" in
    1)
        read -p "Message: " MSG
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        ENCRYPTED=$(echo -n "$MSG" | openssl enc -aes-256-cbc -a -salt -pass pass:"$SEED" -pbkdf2)
        echo "[$TIMESTAMP] OUT: $ENCRYPTED" >> "$VAULT"
        echo -e "\n\e[1;32m✅ Logged to Vault.\e[0m"
        echo -e "Payload: \e[1;34m$ENCRYPTED\e[0m"
        ;;
    2)
        read -p "Paste String: " STRING
        echo -n "Decrypted: "
        echo "$STRING" | openssl enc -aes-256-cbc -d -a -pass pass:"$SEED" -pbkdf2 2>/dev/null
        ;;
    3)
        echo -e "\e[1;33m--- ENCRYPTED TRANSMISSION HISTORY ---\e[0m"
        if [ -f "$VAULT" ]; then cat "$VAULT"; else echo "Vault empty."; fi
        ;;
esac

