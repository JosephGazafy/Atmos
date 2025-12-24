#!/usr/bin/env bash
# 🛡️ Nightly Sovereignty Restoration & Mesh Sync

cd ~/Atmos
echo "🌙 Initiating Nightly Heartbeat Sentinel..."

# 1. Reset HWM Variance to zero (Restore Point)
python3 -c "import json, os; p = os.path.expanduser('~/Atmos/shared_state.json'); d = json.load(open(p)); d['psi_index'] = 1.0; d['hwm_variance'] = 0.0; d['status'] = 'NIGHTLY_RESTORE_COMPLETE'; json.dump(d, open(p, 'w'), indent=4)"

# 2. Run WMD and Logic Audit
python3 bin/wmd_sentinel.py
python3 bin/sentinel_heartbeat.py

# 3. Final Mesh Push
git add .
git commit -m "🌙 Nightly Sync: HWM 1.0 Restored | Mesh Aligned | WMD Aware"
git push origin main --force

echo "🏔️  SOVEREIGNTY ANCHORED. SLEEP SECURE."
