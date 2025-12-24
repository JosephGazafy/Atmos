#!/usr/bin/env python3
import json, os

def update_threat_definitions():
    lib_path = os.path.expanduser("~/Atmos/skill_library.json")
    with open(lib_path, 'r+') as f:
        lib = json.load(f)
        # SAGE Evolution: Incorporating WMD Policy (EO Dec 15, 2025)
        lib['wmd_policy_active'] = True
        lib['threat_signatures'] = ["Illicit_Fentanyl", "Piperidone_Precursor", "Chemical_Weapon_Threat"]
        lib['defense_protocol'] = "WMD_NONPROLIFERATION"
        
        f.seek(0); json.dump(lib, f, indent=4); f.truncate()
    print("🛡️  WMD SENTINEL: Fentanyl classification updated to Weapon of Mass Destruction.")

if __name__ == "__main__":
    update_threat_definitions()
