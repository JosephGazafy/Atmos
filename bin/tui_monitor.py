import curses, json, os, time
def draw(stdscr):
    curses.curs_set(0); stdscr.nodelay(1)
    while True:
        stdscr.clear()
        try:
            with open(os.path.expanduser("/data/data/com.termux/files/home/Atmos/shared_state.json"), 'r') as f: d = json.load(f)
            with open(os.path.expanduser("/data/data/com.termux/files/home/Atmos/skill_library.json"), 'r') as f: l = json.load(f)
            stdscr.addstr(1, 2, f"🛡️  ATMOS SOVEREIGNTY [Lv.{l['self_evolution_count']}]", curses.A_BOLD)
            stdscr.addstr(3, 2, f"Ψ INDEX: {d['psi_index']} | HWM VAR: {d['hwm_variance']}")
            stdscr.addstr(5, 2, f"STATUS: {d['status']} | PULSE: {d['hr_input']} BPM")
            stdscr.addstr(7, 2, "🌾 Truth is never served by the diminishment of the seeker.", curses.A_DIM)
        except: pass
        stdscr.refresh()
        if stdscr.getch() == ord('q'): break
        time.sleep(1)
if __name__ == "__main__": curses.wrapper(draw)
