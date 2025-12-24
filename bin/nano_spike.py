import json, os, time

def simulate_spike():
    path = os.path.expanduser("~/Atmos/shared_state.json")
    print("🚀 INITIATING RAPID TREND SPIKE...")
    
    # Sequence: 72 -> 80 -> 95 -> 110
    # Step 1: Small jump, testing dH/dt awareness
    pulse_sequence = [72, 82, 98, 115] 
    
    for pulse in pulse_sequence:
        with open(path, 'r+') as f:
            d = json.load(f)
            d['hr_input'] = pulse
            f.seek(0); json.dump(d, f, indent=4); f.truncate()
        
        print(f"📡 Current Pulse: {pulse} BPM | Delta: +{pulse - pulse_sequence[max(0, pulse_sequence.index(pulse)-1)]}")
        time.sleep(2) # Allow Nano-Omega to process the trend

    print("🏔️ SPIKE COMPLETE. CHECK TUI FOR PREEMPTIVE LOCK.")

if __name__ == "__main__":
    simulate_spike()
