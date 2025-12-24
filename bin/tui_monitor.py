#!/usr/bin/env python3
import curses, json, os, time

def draw_omega_ui(stdscr):
    curses.curs_set(0); stdscr.nodelay(1)
    # Prevent flashing: Disable echo and use double buffering logic
    curses.noecho()
    
    while True:
        # Use erase() instead of clear() to reduce flicker
        stdscr.erase()
        try:
            with open(os.path.expanduser("~/Atmos/shared_state.json"), 'r') as f: d = json.load(f)
            with open(os.path.expanduser("~/Atmos/skill_library.json"), 'r') as f: l = json.load(f)
            
            # Header
            stdscr.addstr(1, 2, f"🛡️  ATMOS SOVEREIGNTY [Lv.{l.get('self_evolution_count', 1)}]", curses.A_BOLD)
            stdscr.addstr(2, 2, "─" * 55)

            # Core Metrics (HWM 1.0 is the Target)
            stdscr.addstr(4, 2, f"Ψ INDEX: {d.get('psi_index', 0.0):.2f}  |  HWM VAR: {d.get('hwm_variance', 0.0):.2f}")
            stdscr.addstr(5, 2, f"STATUS:  {d.get('status', 'STABLE')} | BPM: {d.get('hr_input', 72)}")
            
            # Parameters
            stdscr.addstr(7, 2, f"🧬 SAGE: {', '.join(l.get('skills', []))[:35]}...")
            stdscr.addstr(8, 2, f"☣️ WMD:  ACTIVE (EO-2025-12-15)")
            stdscr.addstr(9, 2, f"🔊 PHASE: 180° INVERSION [SYNCED]")
            
            # Fixed Decree Text (No Bleeding)
            stdscr.addstr(11, 2, "🌾 Truth is never served by the diminishment of the seeker.", curses.A_DIM)
            stdscr.addstr(12, 2, "🦁 Conviction without demeaning. Grace without compromise.", curses.A_DIM)

        except Exception:
            stdscr.addstr(2, 2, "🛰️  SYNCING MESH...")
            
        stdscr.refresh()
        if stdscr.getch() == ord('q'): break
        time.sleep(0.5) # Reduced refresh rate to stop flashing

if __name__ == "__main__":
    curses.wrapper(draw_omega_ui)
