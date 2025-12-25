import os, time, json, subprocess

def get_git_status():
    try:
        status = subprocess.check_output(["git", "status", "-s"], stderr=subprocess.DEVNULL).decode()
        return "⚠️  Unsynced Changes" if status else "✅ Cloud Synced"
    except:
        return "❌ Git Error"

def draw_gui():
    path = "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"
    try:
        with open(path, 'r') as f:
            data = [json.loads(l) for l in f.readlines()]
    except:
        data = []

    latest = data[-1] if data else {"altitude": 0, "density": 0, "pressure": 0, "timestamp": "N/A"}
    os.system('clear')
    
    print(f"┏━━━━ ATMOS SOVEREIGN INTERFACE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"┃ SYSTEM: {get_git_status():<25} | UTC: {time.strftime('%H:%M:%S')} ┃")
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ [1] PHYSICS TELEMETRY                                     ┃")
    print(f"┃     Altitude: {latest['altitude']:>8} m      Density: {latest['density']:>8.4f}  ┃")
    print(f"┃     Pressure: {latest['pressure']:>8.2f} Pa     Time: {latest['timestamp'][11:19]}    ┃")
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ [2] DATA ANALYSIS                                         ┃")
    print(f"┃     Total Records: {len(data):<6} | Logs: /Atmos/Atmos/Atmos/   ┃")
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print(f"┃ [3] SECURITY & ALERTS                                     ┃")
    if os.path.exists("alerts.log"):
        with open("alerts.log", "r") as f:
            last_alert = f.readlines()[-1:]
            msg = last_alert[0].strip() if last_alert else "No Recent Anomalies"
            print(f"┃     LAST: {msg[:47]:<47} ┃")
    else:
        print(f"┃     Status: All Systems Nominal                           ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("  COMMANDS: [atmos-check] [make sweep] [make search D=0.x]")

if __name__ == "__main__":
    try:
        while True:
            draw_gui()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nGUI Terminated.")

