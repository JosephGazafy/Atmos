#!/usr/bin/env bash
# Sovereign Auto-Start
nohup python3 ~/Atmos/bin/atmos_omega.py > /dev/null 2>&1 &
nohup python3 ~/Atmos/bin/atmos_doctor.py > /dev/null 2>&1 &
echo "🛡️  ATMOS OMEGA: All processes synchronized and running in background."
