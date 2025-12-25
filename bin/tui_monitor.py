#!/usr/bin/env python3
import curses, json, os, time

def draw_reformer_ui(stdscr):
    curses.curs_set(0); stdscr.nodelay(1)
    while True:
        stdscr.erase()
        try:
            with open(os.path.expanduser("~/Atmos/shared_state.json"), 'r') as f: d = json.load(f)
            with open(os.path.expanduser("~/Atmos/skill_library.json"), 'r') as f: l = json.load(f)
            
            # Header with Reformer Context
            stdscr.addstr(1, 2, f"🛡️  REFORMER-SOVEREIGNTY [Bucket: {d.get('lsh_bucket', 'N/A')}]", curses.A_BOLD)
            stdscr.addstr(2, 2, "─" * 55)

            # Core Metrics
            stdscr.addstr(4, 2, f"Ψ INDEX: {d.get('psi_index', 0.0):.3f} | HWM VAR: {d.get('hwm_variance', 0.0):.3f}")
            stdscr.addstr(6, 2, f"STATUS:  {d.get('status', 'LOADING...')} | BPM: {d.get('hr_input', 72)}")
            
            # Reformer Detail
            stdscr.addstr(8, 2, f"🧩 CRIME/PUNISHMENT: Window Active (524k Context)")
            stdscr.addstr(9, 2, f"☣️ WMD POLICY: {d.get('wmd_status', 'ENFORCED [EO-2025-12-15]')}")
            
            # The Decree
            stdscr.addstr(11, 2, "🌾 Truth is never served by the diminishment of the seeker.", curses.A_DIM)
            stdscr.addstr(12, 2, "🦁 Grace is the anchor; Conviction is the shield.", curses.A_DIM)

        except:
            stdscr.addstr(2, 2, "🛰️  RECONSTITUTING BUCKETS...")
            
        stdscr.refresh()
        if stdscr.getch() == ord('q'): break
        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(draw_reformer_ui)
