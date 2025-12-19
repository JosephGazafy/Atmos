#!/bin/bash
# ATMOS CORE v3.0 - MESH INVITATION PROTOCOL
./logo.sh

# The Master One-Liner for your friend to join the US-East Mesh
INVITE_CMD="pkg install curl -y && curl -LO https://raw.githubusercontent.com/JosephGazafy/Atmos/main/update.sh && chmod +x update.sh && ./update.sh"

echo -e "\e[1;35m📡 GENERATING MESH INVITATION...\e[0m"
echo "----------------------------------------------------"
echo "Scan this code with a camera to copy the Auto-Join command:"
echo ""

# Generate the QR Code in the terminal
echo "$INVITE_CMD" | qrencode -t ANSI256

echo ""
echo "----------------------------------------------------"
echo -e "\e[1;32m✅ INVITATION ACTIVE\e[0m"
echo "Direct your peer to paste the result into their Termux."

