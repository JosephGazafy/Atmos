#!/usr/bin/env bash
# ATMOS ATLAS-01 MASTER STARTUP v490.0

echo ">> INITIALIZING 2026 SOVEREIGN ENVIRONMENT..."

# 1. Bind TTY and Identity
export GPG_TTY=$(tty)
export PYTHONPATH=$PYTHONPATH:~/Atmos/src
export SOVEREIGN_FPR=$(gpg --list-secret-keys --with-colons | grep fpr | cut -d: -f10 | head -n 1)

# 2. Run Diagnostic
python3 ~/Atmos/bin/atmos_doctor.py

# 3. Start Autopilot Sentinel
echo ">> LAUNCHING AUTOPILOT..."
python3 ~/Atmos/src/atmos/main.py --mode sentinel --veracity-check

