import os
import time
import json

def clear():
    os.system('clear')

def get_data():
    path = "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
            return [json.loads(l) for l in lines]
    except:
        return []

def draw_gui():
    data = get_data()
    latest = data[-1] if data else {"altitude": 0, "density": 0, "pressure": 0, "timestamp": "N/A"}
    
    clear()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                 ATMOS SOVEREIGN GUI v2.0                  ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    
    print(f"  [ LIVE TELEMETRY ]")
    print(f"  🛰️  Altitude:  {latest['altitude']:>10} m")
    print(f"  🌡️  Density:   {latest['density']:>10.4f} kg/m³")
    print(f"  🌀 Pressure:  {latest['pressure']:>10.2f} Pa")
    print(f"  🕒 Timestamp: {latest['timestamp'][:19]}")
    print("  " + "─"*55)
    
    print(f"  [ HISTORICAL STATS ]")
    print(f"  📊 Total Records: {len(data)}")
    avg_p = sum(d['pressure'] for d in data) / len(data) if data else 0
    print(f"  📉 Avg Pressure:  {avg_p:>10.2f} Pa")
    print("  " + "─"*55)

    print(f"  [ SYSTEM ALERTS ]")
    if os.path.exists("alerts.log"):
        with open("alerts.log", 'r') as f:
            alerts = f.readlines()[-3:] # Show last 3 alerts
            for a in alerts:
                print(f"  ⚠️  {a.strip()[:50]}")
    else:
        print("  ✅ No active anomalies detected.")
    
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(" [ Ctrl+C to Exit ] | [ Run 'make sweep' in background to update ]")

if __name__ == "__main__":
    try:
        while True:
            draw_gui()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting GUI...")

