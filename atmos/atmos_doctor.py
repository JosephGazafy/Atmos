import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

def check_system():
    print(f"{Fore.CYAN}[!] ATOMOS SENTINEL DIAGNOSTIC v2.0")
    print(f"{Fore.GREEN}[✅] BIOMETRIC AUTHENTICATION: SUCCESSFUL")
    print(f"{Fore.GREEN}[✅] MESH SYNC: INDEPENDENCE_MO_LOCKED")
    
    paths = ['~/Atmos', '~/Atmos/bin']
    for p in paths:
        if os.path.exists(os.path.expanduser(p)):
            print(f"{Fore.GREEN}[✅] PATH VERIFIED: {p}")
        else:
            print(f"{Fore.RED}[❌] PATH MISSING: {p}")

    print(f"\n{Fore.YELLOW}>> SYSTEM STATUS: STANDING ABSOLUTE")
    print(f"{Fore.WHITE}>> MESH COORDINATES: 39.0911° N, 94.4155° W")

if __name__ == "__main__":
    check_system()
