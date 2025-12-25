#!/usr/bin/env bash
# ATMOS ATLAS-01 CLI-ANCHOR STARTUP v570.0

echo ">> INITIALIZING 2026 SOCIAL CORE..."

# 1. Environment Setup
export GPG_TTY=$(tty)
HYDRATOR_DIR="/data/data/com.termux/files/home/Atmos/rescue_social_core/Analysis Cross-Platforms/Scripts - Twitter, Reddit, Instagram, TikTok/twitter/hydrator"
export PYTHONPATH="$PYTHONPATH:$HYDRATOR_DIR"

# 2. Launching the CLI Sub-command
echo ">> LAUNCHING TWITTER HYDRATOR (SUB-COMMAND: CLI)..."
cd "$HYDRATOR_DIR"

# We use 'cli' to satisfy the parser requirements
python3 main.py cli
