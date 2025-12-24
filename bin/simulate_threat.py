#!/usr/bin/env python3
import json, os, time

def run_simulation():
    state_p = os.path.expanduser("~/Atmos/shared_state.json")
    
    print("🦁 TRIGGERING JUDAH SHIELD...")
    with open(state_p, 'r+') as f:
        data = json.load(f)
        data['hr_input'] = 115  # Trigger Threshold
        f.seek(0); json.dump(data, f, indent=4); f.truncate()
    
    print("☣️ WMD DEFENSE ACTIVE. Check your TUI Monitor.")
    time.sleep(15)
    
    print("🌾 RESTORING JOSEPH ANCHOR...")
    with open(state_p, 'r+') as f:
        data = json.load(f)
        data['hr_input'] = 62  # Return to Grace
        f.seek(0); json.dump(data, f, indent=4); f.truncate()
    print("🏔️  HWM RECOVERY INITIATED.")

if __name__ == "__main__":
    run_simulation()
