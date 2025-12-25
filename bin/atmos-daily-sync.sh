#!/bin/bash
# Load environment
source ~/.bashrc
cd ~/Atmos

# Run the Harvest
~/Atmos/bin/atmos-start

# Push to GitHub
git add .
git commit -m "Automated Daily Sync: Independence MO Forensic Record [$(date +%Y-%m-%d)]"
git push origin main
