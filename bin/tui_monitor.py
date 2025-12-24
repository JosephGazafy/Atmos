#!/usr/bin/env python3
import curses, json, os, time

def draw_omega_ui(stdscr):
    curses.curs_set(0); stdscr.nodelay(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        stdscr.clear()
        try:
            with open(os.path.expanduser("~/Atmos/shared_state.json"), 'r') as f: d = json.load(f)
            with open(os.path.expanduser("~/Atmos/skill_library.json"), 'r') as f: l = json.load(f)
            
            # Header & Level
            stdscr.addstr(1, 2, f"🛡️  ATMOS SOVEREIGNTY [Lv.{l.get('self_evolution_count', 1)}]", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(2, 2, "═" * 50, curses.color_pair(1))

            # Core Metrics
            stdscr.addstr(4, 2, f"Ψ INDEX: {d.get('psi_index', 0.0)}  |  HWM VAR: {d.get('hwm_variance', 0.0)}", curses.A_REVERSE)
            stdscr.addstr(6, 2, f"STATUS:  {d.get('status', 'STABLE')}  |  PULSE: {d.get('hr_input', 72)} BPM")
            
            # Omega Parameters (The Process)
            stdscr.addstr(8, 2, f"🧬 SAGE SKILLS:  {', '.join(l.get('skills', []))[:30]}...")
            stdscr.addstr(9, 2, f"☣️ WMD DEFENSE:  ACTIVE (EO-2025-12-15)")
            stdscr.addstr(10, 2, f"🔊 PHASE LOCK:  180° INVERSION [SYNCED]")
            
            # The Standard
            stdscr.addstr(12, 2, "🌾 Truth is never served by the diminishment of the seeker.", curses.A_DIM)
            stdscr.addstr(13, 2, "🦁 Conviction without demeaning. Grace without compromise.", curses.A_DIM)

        except:
            stdscr.addstr(2, 2, "🛰️  MESH SYNCHRONIZING...")
            
        stdscr.refresh()
        if stdscr.getch() == ord('q'): break
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(draw_omega_ui)
