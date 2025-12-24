#!/usr/bin/env python3
import json, os, time, subprocess

def sync_all():
    base_dir = os.path.expanduser("~/Atmos")
    state_p = f"{base_dir}/shared_state.json"
    lib_p = f"{base_dir}/skill_library.json"
    
    while True:
        try:
            # 1. Load Data
            with open(state_p, 'r') as f: d = json.load(f)
            with open(lib_p, 'r') as f: l = json.load(f)
            
            # 2. Automated Biometric-Logic Sweep (Filter of Judah)
            bpm = d.get('hr_input', 72)
            # WMD Awareness: High pulse + WMD policy = Defensive Lock
            if bpm > 110 and l.get('wmd_policy_active'):
                d['ternary_state'] = -1
                d['status'] = "WMD_DEFENSE_ACTIVE"
            else:
                d['ternary_state'] = 1 if bpm < 65 else 0
                d['status'] = "ELEVATED_GRACE"

            # 3. SAGE Learning Integration
            l_gain = l.get("self_evolution_count", 1) * 0.01
            d['psi_index'] = round(min(1.0, 0.98 + l_gain), 3)
            d['hwm_variance'] = round(d['psi_index'] - 1.0, 4)

            # 4. Save & Sync
            with open(state_p, 'w') as f: json.dump(d, f, indent=4)
            
            # 5. Automated Mesh Heartbeat (Every 300s)
            if int(time.time()) % 300 == 0:
                subprocess.run([f"{base_dir}/bin/mesh_push_all.sh"], capture_output=True)
                
        except Exception as e:
            print(f"Sync Divergence: {e}")
        
        time.sleep(2)

if __name__ == "__main__":
    sync_all()
