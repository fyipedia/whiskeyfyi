"""MCP server for whiskeyfyi — whiskey knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install whiskeyfyi[mcp]``

Run as a standalone server::

    python -m whiskeyfyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "whiskeyfyi": {
                "command": "python",
                "args": ["-m", "whiskeyfyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("whiskeyfyi")


@mcp.tool()
def whiskey_search(query: str) -> str:
    """Search whiskeys, distilleries, and glossary terms from WhiskeyFYI.

    Searches across whiskey types, distilleries, regions, cask types,
    expressions, and terminology.

    Args:
        query: Search term (e.g. "bourbon", "Lagavulin", "single malt").
    """
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        results = api.search(query)

    items = results.get("results", [])
    count = results.get("count", 0)

    lines = [
        f"## Whiskey Search: {query}",
        "",
        f"Found **{count}** results.",
        "",
    ]

    if items:
        lines.extend(
            [
                "| Type | Name | URL |",
                "|------|------|-----|",
            ]
        )
        for item in items:
            item_type = item.get("type", "")
            name = item.get("name", "")
            url = item.get("url", "")
            lines.append(f"| {item_type} | {name} | {url} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
