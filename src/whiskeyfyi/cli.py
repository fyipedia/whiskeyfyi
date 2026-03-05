"""Command-line interface for whiskeyfyi.

Requires the ``cli`` extra: ``pip install whiskeyfyi[cli]``

Usage::

    whiskeyfyi search "bourbon"
    whiskeyfyi search "Lagavulin"
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="whiskeyfyi",
    help="Whiskey knowledge API client — search whiskey types, distilleries, and terms.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'bourbon', 'Lagavulin')"),
) -> None:
    """Search whiskeys, distilleries, and glossary terms."""
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        results = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name")
    table.add_column("URL")

    for item in results.get("results", []):
        table.add_row(
            item.get("type", ""),
            item.get("name", ""),
            item.get("url", ""),
        )

    console.print(table)
    console.print(f"[dim]{results.get('count', 0)} results[/dim]")


if __name__ == "__main__":
    app()
