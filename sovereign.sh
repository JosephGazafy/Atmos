#!/bin/bash
./logo.sh
case "$1" in
    "boot") go mod tidy && chmod +x *.sh ;;
    "mesh") CGO_ENABLED=0 go run main.go ;;
    "shield") python3 sovereign_init.py ;;
    "shadow") history -c && chmod 400 * ;;
    *) echo "Usage: ./sovereign.sh {boot|mesh|shield|shadow}" ;;
esac

