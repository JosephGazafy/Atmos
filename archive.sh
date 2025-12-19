#!/bin/bash
# ATMOS CORE v3.0 - SECURE ARCHIVE PROTOCOL
./logo.sh

TIMESTAMP=$(date '+%Y%m%d')
ARCHIVE_NAME="Atmos_Core_v3_$TIMESTAMP.tar.gz.gpg"
SEED="origin-anchor-Judah-Joseph-180-phase-deciduous-stride-equitable-coefficient-archetypal-mesh-vivus-philo-navi-ping"

echo -e "\e[1;35m📦 PACKAGING SOVEREIGN ASSETS...\e[0m"

# 1. Create a compressed tarball, excluding logs and temporary files
tar -czf - --exclude='.git' --exclude='*.log' --exclude='.atmos_vault*' ~/Atmos | \
gpg --batch --yes --passphrase "$SEED" --symmetric --cipher-algo AES256 -o "$ARCHIVE_NAME"

if [ $? -eq 0 ]; then
    echo -e "\e[1;32m✅ ARCHIVE CREATED: $ARCHIVE_NAME\e[0m"
    echo "----------------------------------------------------"
    echo "⚠️  ACTION REQUIRED: Move this file to a secondary location"
    echo "then run './slough.sh' to remove the local copy."
else
    echo -e "\e[1;31m❌ ARCHIVE FAILED\e[0m"
fi

