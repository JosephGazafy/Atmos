#!/bin/bash
./logo.sh
echo -e "\e[1;35m🚀 ENGAGING AUTOPILOT...\e[0m"
./scuttle.sh &
crond > /dev/null 2>&1
./registry.sh
./sovereign.sh mesh
