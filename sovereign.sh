#!/bin/bash
# ATMOS CORE v3.0 - MASTER CONTROLLER
./logo.sh

case "$1" in
    "autopilot") ./autopilot.sh ;;
    "status") ./status.sh ;;
    "invite") ./invite.sh ;;
    "check") chmod +x mesh_check.sh && ./mesh_check.sh ;;
    "mesh") ./alert_sentinel.sh ;;
    "update") ./update.sh ;;
    "shadow") history -c && chmod 400 * ;;
    *) echo "Usage: ./sovereign.sh {autopilot|status|invite|check|mesh|update|shadow}" ;;
esac

