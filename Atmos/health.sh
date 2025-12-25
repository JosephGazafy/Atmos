



#!/data/data/com.termux/files/usr/bin/bash
PROJ_DIR="/data/data/com.termux/files/home/Atmos/Atmos/Atmos"
export PYTHONPATH="$PYTHONPATH:$PROJ_DIR/src"
cd "$PROJ_DIR"

echo "--- 🔍 Atmos Sovereignty Health Check ---"

# 1. Run Engine
python -m atmos.main -a 1000 -j || echo "❌ Python logic error"

# 2. Run Go Scanner
./system/sovereign/sovereign_tool || echo "❌ Go binary error"

# 3. Update Dashboard
COUNT=$(wc -l < data.json 2>/dev/null || echo "0")
sed -i "s/Last Sync:.*/Last Sync:  $(date)/" welcome.txt
sed -i "s/Data Count:.*/Data Count: $COUNT/" welcome.txt

# 4. Global Push
pkg update && pkg upgrade -y
git add .
git commit -m "Dashboard Update: $COUNT records logged"
git push origin Master --force-with-lease

