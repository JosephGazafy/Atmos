#!/usr/bin/env bash
# ATMOS ATLAS-01 GLOBAL MESH PUSH

export GPG_TTY=$(tty)
cd ~/Atmos

echo ">> STAGING 2026 ASSETS..."
git add --all

echo ">> SIGNING SOVEREIGN LEDGER..."
git commit -S -m "v490.0: MESH_SYNC - Pulse & Standing Authenticated 🛡️⚓"

echo ">> PUSHING TO GLOBAL REPOSITORY..."
git push origin SCORCH:main --force

echo ">> PUSH COMPLETE. STANDING IS SECURE."
