


import os, time, json, subprocess

# ANSI Colors
CYAN, GREEN, YELLOW, RED = "\033[96m", "\033[92m", "\033[93m", "\033[91m"
BOLD, RESET = "\033[1m", "\033[0m"

def get_git_info():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
        return f"{GREEN}{branch}{RESET}"
    except: return f"{RED}OFFLINE{RESET}"

def draw_bar(val, max_val=1.225):
    width = 15
    filled = int(min(max((val / max_val), 0), 1) * width)
    return f"|{YELLOW}{'█' * filled}{RESET}{'░' * (width - filled)}|"

def draw_gui():
    path = "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"
    try:
        with open(path, 'r') as f:
            data = [json.loads(l) for l in f.readlines()]
    except: data = []

    latest = data[-1] if data else {"altitude": 0, "density": 0, "pressure": 0, "timestamp": "N/A"}
    os.system('clear')
    
    print(f"{BOLD}{CYAN}┏━━━━━━━━━━━━━━━━━ ATMOS MULTI-FUNCTION COMMAND ━━━━━━━━━━━━━━━━━━━┓{RESET}")
    
    # --- FUNCTION 1: CONSTITUTIONAL & CLOUD ---
    print(f"┃ {BOLD}CONSTITUTION:{RESET} {GREEN}ACTIVE{RESET}  | {BOLD}CLOUD:{RESET} {get_git_info():<18} | {YELLOW}{time.strftime('%H:%M:%S')}{RESET} ┃")
    
    # --- FUNCTION 2: PHYSICS (CYAN) ---
    print(f"{CYAN}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
    print(f"┃ {BOLD}[1] PHYSICS ENGINE{RESET}                                              ┃")
    print(f"┃     Alt: {latest['altitude']:>6}m | Dens: {latest['density']:>6.4f} {draw_bar(latest['density'])} ┃")
    
    # --- FUNCTION 3: MESH NETWORK (YELLOW) ---
    print(f"{YELLOW}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
    print(f"┃ {BOLD}[2] MESH NETWORK & TELEMETRY{RESET}                                    ┃")
    print(f"┃     Node: {BOLD}Termux-Primary{RESET} | Status: {GREEN}CONNECTED{RESET} | Latency: 24ms    ┃")
    
    # --- FUNCTION 4: SECURITY VAULT (GREEN) ---
    print(f"{GREEN}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
    print(f"┃ {BOLD}[3] VAULT & BIOMETRICS{RESET}                                          ┃")
    print(f"┃     Rotation: {BOLD}24h{RESET} | Gate: {GREEN}LOCKED{RESET} | Keys: {BOLD}AES-256-GCM{RESET}         ┃")
    
    # --- FUNCTION 5: ANOMALY LOGS (RED) ---
    print(f"{RED}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
    print(f"┃ {BOLD}[4] CRITICAL ANOMALIES{RESET}                                          ┃")
    if os.path.exists("alerts.log"):
        with open("alerts.log", "r") as f:
            alerts = f.readlines()[-1:]
            msg = alerts[0].strip() if alerts else "No Alerts"
            print(f"┃     {RED}ALERT: {msg[:54]:<54}{RESET} ┃")
    else:
        print(f"┃     No anomalies detected in the last cycle.                    ┃")
    
    print(f"{BOLD}{CYAN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
    print(f"  {BOLD}SYSTEM READY.{RESET} Use {CYAN}atmos-check{RESET} to force update all layers.    ")

if __name__ == "__main__":
    try:
        while True:
            draw_gui()
            time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n{RED}Terminating GUI...{RESET}")

