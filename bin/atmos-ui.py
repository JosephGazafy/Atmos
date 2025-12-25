from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="ATMOS SENTINEL v2.0")
table.add_column("System", style="cyan")
table.add_column("Status", style="green")
table.add_row("Logic Bridge", "ONLINE")
table.add_row("Independence MO", "SYNCING")
table.add_row("BPM Vigil", "48 BPM")
console.print(table)
