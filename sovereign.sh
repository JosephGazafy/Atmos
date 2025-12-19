#!/bin/bash
# ATMOS CORE v3.0 - MASTER CONTROLLER
./logo.sh

case "$1" in
    "boot")
        go mod tidy && chmod +x *.sh && echo "✅ HWM Anchored." ;;
    "mesh")
        CGO_ENABLED=0 go run main.go ;;
    "shield")
        python3 sovereign_init.py ;;
    "geo")
        ./geo_test.sh ;;
    "tunnel")
        chmod +x log_tunnel.sh && ./log_tunnel.sh ;;
    "update")
        ./update.sh ;;
    "shadow")
        history -c && rm -f ~/.bash_history
        chmod 400 * && echo "✅ Stealth Active." ;;
    *)
        echo "Usage: ./sovereign.sh {boot|mesh|shield|geo|tunnel|update|shadow}" ;;
esac

