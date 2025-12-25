#!/data/data/com.termux/files/usr/bin/bash
echo "--- 🔍 Atmos Sovereignty Health Check ---"

# Check Python
if python -c "import atmos; print('✅ Python Core Linked')" &> /dev/null; then
    python -m atmos.main -a 1000 -j
else
    echo "❌ Python Link Broken"
fi

# Check Go
if [ -f "./system/sovereign/sovereign_tool" ]; then
    echo "✅ Go Binary Found"
    ./system/sovereign/sovereign_tool
else
    echo "⚠️  Go Binary Missing. Run 'make build-go'"
fi

