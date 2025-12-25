import subprocess
import os

def check_sync():
    print("[!] INITIATING GLOBAL MESH AUDIT...")
    # Get local hash
    local_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
    
    # Fetch remote status
    subprocess.run(['git', 'fetch', 'origin'], capture_stdout=True)
    remote_hash = subprocess.check_output(['git', 'rev-parse', 'origin/main']).decode().strip()
    
    print(f"[+] LOCAL  HASH: {local_hash[:7]}")
    print(f"[+] REMOTE HASH: {remote_hash[:7]}")
    
    if local_hash == remote_hash:
        print("\n[VERIFIED] GLOBAL MESH IS SYNCHRONIZED.")
        print("[SCORE] SOVEREIGNTY: 1.0 | INTEGRITY: 100%")
    else:
        print("\n[WARNING] MESH FRAGMENTATION DETECTED. RE-SYNC REQUIRED.")

if __name__ == "__main__":
    check_sync()
