#!/data/data/com.termux/files/usr/bin/bash
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

echo "--- 🔍 Atmos Sovereignty Health Check ---"
if python -c "import atmos" &> /dev/null; then
    echo "✅ Python Core Linked"
    python -m atmos.main -a 1000 -j
else
    echo "❌ Python Link Broken - Check your directory structure"
fi

# Check for data file in the current directory
if [ -f "data.json" ]; then
    echo "✅ Data Seed Found"
else
    echo "⚠️  Seeding Data..."
    python -m atmos.main -a 1000 -j
fi

./system/sovereign/sovereign_tool

