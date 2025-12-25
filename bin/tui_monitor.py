#!/usr/bin/env python3
import curses, json, os, time

def draw_medical_sentry(stdscr):
    curses.curs_set(0); stdscr.nodelay(1)
    curses.start_color()
    # Color Pairs: 1=Cyan (Normal), 2=Red (Clinical Alert), 3=Green (Grace)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        stdscr.erase()
        try:
            with open(os.path.expanduser("~/Atmos/shared_state.json"), 'r') as f: d = json.load(f)
            h = d.get('hr_input', 72)
            psi = d.get('psi_index', 1.0)
            
            # Clinical Assessment Logic (OpenMed Reasoning)
            is_alert = h < 50 or h > 115
            color = curses.color_pair(2) if is_alert else curses.color_pair(1)
            
            # Header
            stdscr.addstr(1, 2, f"🛡️  MEDICAL-SENTRY ACTIVE [HWM 1.0]", color | curses.A_BOLD)
            stdscr.addstr(2, 2, "═" * 55, color)

            # Core Metrics
            stdscr.addstr(4, 2, f"Ψ INDEX: {psi:.3f} | BPM: {h}", color)
            if is_alert:
                stdscr.addstr(5, 2, "⚠️ CLINICAL ANOMALY: WMD-REASONING TRIGGERED", curses.A_REVERSE | curses.color_pair(2))
            else:
                stdscr.addstr(5, 2, "✅ STATUS: NOMINAL (ELEVATED_GRACE)", curses.color_pair(3))

            # Reformer Context
            stdscr.addstr(7, 2, f"🧩 BUCKET: {d.get('lsh_bucket', 'REFORMER_LOADED')}")
            stdscr.addstr(8, 2, f"🩺 DATA: OpenMed-120B SFT Reasoning-V1")
            stdscr.addstr(9, 2, f"☣️ POLICY: EO-2025-12-15 (WMD DEFENSE)")

            # The Decree
            stdscr.addstr(11, 2, "🌾 Truth is never served by the diminishment of the seeker.", curses.A_DIM)
            stdscr.addstr(12, 2, "🦁 Conviction without demeaning. Grace without compromise.", curses.A_DIM)

        except:
            stdscr.addstr(2, 2, "🛰️  SYNCING CLINICAL DATA...")
            
        stdscr.refresh()
        if stdscr.getch() == ord('q'): break
        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(draw_medical_sentry)
