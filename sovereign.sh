#!/bin/bash
# ATMOS CORE v3.0 - MASTER CONTROLLER
./logo.sh

case "$1" in
    "boot")
        go mod tidy && chmod +x *.sh && echo "✅ HWM Anchored." ;;
    "mesh")
        chmod +x alert_sentinel.sh && ./alert_sentinel.sh ;;
    "shield")
        python3 sovereign_init.py ;;
    "geo")
        ./geo_test.sh ;;
    "tunnel")
        ./log_tunnel.sh ;;
    "update")
        ./update.sh ;;
    "shadow")
        history -c && rm -f ~/.bash_history
        chmod 400 * && echo "✅ Stealth Active. Files Locked." ;;
    *)
        echo "Usage: ./sovereign.sh {boot|mesh|shield|geo|tunnel|update|shadow}" ;;
esac

