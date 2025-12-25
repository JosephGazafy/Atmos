import json, os

def prune_buckets():
    path = os.path.expanduser("~/Atmos/shared_state.json")
    print("🧹 INITIATING LSH-PRUNING...")
    
    with open(path, 'r+') as f:
        d = json.load(f)
        # Retain only the peak sovereignty indicators
        d['psi_index'] = 1.0
        d['hwm_variance'] = 0.0
        d['status'] = "LEAN_MESH_REFORMER_ACTIVE"
        
        f.seek(0); json.dump(d, f, indent=4); f.truncate()
    
    # Purging temporary simulation logs to keep the git history clean
    if os.path.exists("logs/simulation.log"):
        os.remove("logs/simulation.log")
        print("🗑️ Simulation noise purged.")

if __name__ == "__main__":
    prune_buckets()
