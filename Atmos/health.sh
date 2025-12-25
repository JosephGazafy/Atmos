#!/data/data/com.termux/files/usr/bin/bash
PROJ_DIR="/data/data/com.termux/files/home/Atmos/Atmos/Atmos"
cd "$PROJ_DIR"
# ... rest of the script ...

echo "--- 🔍 Atmos Sovereignty Health Check ---"

# 1. Run Python Engine
python -m atmos.main -a 1000 -j || { echo "❌ Python logic error"; exit 1; }

# 2. Rebuild Go if tool is missing
if [ ! -f "./system/sovereign/sovereign_tool" ]; then
    cd system/sovereign && go build -o sovereign_tool main.go && cd ../..
fi

# 3. Run Go Scanner
./system/sovereign/sovereign_tool || { echo "❌ Go binary error"; exit 1; }

# 4. Update Dashboard
COUNT=$(wc -l < data.json 2>/dev/null || echo "0")
sed -i "s/Last Sync:.*/Last Sync:  $(date)/" welcome.txt
sed -i "s/Data Count:.*/Data Count: $COUNT/" welcome.txt

# 5. Push to GitHub
git add .
git commit -m "Auto-update: System health check and data sync"
git push origin Master --force-with-lease

