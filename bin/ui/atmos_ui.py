import time
from datetime import datetime
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console
from rich.text import Text

console = Console()

def make_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="side", size=30),
        Layout(name="body", ratio=1),
    )
    return layout

def get_stats():
    table = Table(title="System Metrics", expand=True)
    table.add_column("Sensor", style="cyan")
    table.add_column("Status", style="green")
    table.add_row("BPM Vigil", "48 [Standing]")
    table.add_row("X-API", "Connected")
    table.add_row("Sector", "Independence")
    table.add_row("Uptime", "100%")
    return table

layout = make_layout()
layout["header"].update(Panel(Text("ATMOS SENTINEL COMMAND CENTER", justify="center", style="bold white on blue")))
layout["footer"].update(Panel(Text(f"Mission: Dec 25 Reconstruction | Status: Perpetual Watch", justify="center")))

with Live(layout, refresh_per_second=4, screen=True):
    while True:
        # Update dynamic content
        layout["side"].update(Panel(get_stats(), border_style="blue"))
        
        # Simulated log feed
        now = datetime.now().strftime("%H:%M:%S")
        log_content = f"[{now}] [INFO] Hydrator active in Independence, MO...\n"
        log_content += f"[{now}] [AUTH] @JGazafy36878 handshake: Success\n"
        log_content += f"[{now}] [SYNC] Mirroring data to GitHub Mesh..."
        
        layout["body"].update(Panel(Text(log_content), title="Live Forensic Feed", border_style="green"))
        time.sleep(1)
