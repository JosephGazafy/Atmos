#!/data/data/com.termux/files/usr/bin/bash
# Absolute path discovery
SCRIPT_DIR="/data/data/com.termux/files/home/Atmos/Atmos/Atmos"
export PYTHONPATH="$PYTHONPATH:$SCRIPT_DIR/src"
cd "$SCRIPT_DIR"

echo "--- 🔍 Atmos Sovereignty Health Check ---"
if python -c "import atmos" &> /dev/null; then
    echo "✅ Python Core Linked"
    python -m atmos.main -a 1000 -j
else
    echo "❌ Python Link Broken"
fi

if [ -f "system/sovereign/sovereign_tool" ]; then
    echo "✅ Go Binary Found"
    ./system/sovereign/sovereign_tool
else
    echo "⚠️  Go Binary Missing. Building now..."
    make build-go
    ./system/sovereign/sovereign_tool
fi

# Auto-Sync Logic
if [[ $(git status --porcelain data.json) ]]; then
    echo "💾 New Data Detected. Synchronizing with Cloud..."
    git add data.json
    git commit -m "Auto-update: Atmospheric logs $(date)"
    git push origin Master --force-with-lease
    echo "✅ Cloud Sync Complete."
fi

