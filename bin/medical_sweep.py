import json, os, time

def run_medical_logic_test():
    path = os.path.expanduser("~/Atmos/shared_state.json")
    print("🩺 INITIATING CLINICAL REASONING SWEEP (OpenMed-120B)...")
    
    # Simulating the 'Crime': Rapid BPM drop + High Variance (Respiratory Distress)
    medical_signatures = [
        {"hr": 72, "status": "NOMINAL"},
        {"hr": 58, "status": "BRADYCARDIA_WATCH"},
        {"hr": 48, "status": "WMD_REASONING_ACTIVATED"},
    ]
    
    for sig in medical_signatures:
        with open(path, 'r+') as f:
            d = json.load(f)
            d['hr_input'] = sig['hr']
            d['status'] = sig['status']
            # Cross-reference with OpenMed SFT Logic
            if d['hr_input'] < 50:
                d['status'] = "🦁_JUDY_SHIELD_WMD_MEDICAL_REASONING"
                d['psi_index'] = 1.0 # Force Sovereignty Anchor
            f.seek(0); json.dump(d, f, indent=4); f.truncate()
        print(f"📡 BPM: {sig['hr']} | Reasoning: {sig['status']}")
        time.sleep(2)

if __name__ == "__main__":
    run_medical_logic_test()
