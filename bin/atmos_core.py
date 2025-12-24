import json, os, time
def run():
    state_p = os.path.expanduser("/data/data/com.termux/files/home/Atmos/shared_state.json")
    while True:
        try:
            with open(state_p, 'r+') as f:
                d = json.load(f)
                bpm = d.get('hr_input', 72)
                # Filter of Judah/Joseph
                t_state = -1 if bpm > 105 else (1 if bpm < 65 else 0)
                # Anti-Paranoia: If High Pulse but No Threat, force Grace
                if bpm > 110: t_state = 0; d['status'] = "RESONANCE_RECOVERY"
                d['ternary_state'] = t_state
                d['psi_index'] = round(min(1.0, 0.95 + (0.01 * t_state)), 3)
                f.seek(0); json.dump(d, f, indent=4); f.truncate()
        except: pass
        time.sleep(1)
if __name__ == "__main__": run()
