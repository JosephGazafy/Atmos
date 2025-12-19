#!/bin/bash
# ATMOS CORE v3.0 - MASTER CONTROLLER
./logo.sh

case "$1" in
    "autopilot") ./autopilot.sh ;;
    "status") ./status.sh ;;
    "invite") chmod +x invite.sh && ./invite.sh ;;
    "mesh") ./alert_sentinel.sh ;;
    "tunnel") ./log_tunnel.sh ;;
    "update") ./update.sh ;;
    "shadow") history -c && chmod 400 * ;;
    *) echo "Usage: ./sovereign.sh {autopilot|status|invite|mesh|tunnel|update|shadow}" ;;
esac

