#!/bin/bash
# ATMOS CORE v3.0 - BIOMETRIC GATE RESTORATION
./logo.sh

echo -e "\e[1;34m[CHECKING HARDWARE SENSORS...]\e[0m"

# Test if Termux:API is functional
if command -v termux-camera-photo &> /dev/null; then
    ./bio_verify ~/Atmos/tmp_bio.jpg && exit 0
else
    echo -e "\e[1;31m[!] HARDWARE SENSOR NOT DETECTED.\e[0m"
    echo -e "\e[1;33mUse: ~/Atmos/emergency.sh to proceed.\e[0m"
    exit 1
fi
