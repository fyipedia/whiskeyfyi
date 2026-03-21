"""MCP server for whiskeyfyi — AI assistant tools for whiskeyfyi.com.

Run: uvx --from "whiskeyfyi[mcp]" python -m whiskeyfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WhiskeyFYI")


@mcp.tool()
def list_expressions(limit: int = 20, offset: int = 0) -> str:
    """List expressions from whiskeyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        data = api.list_expressions(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No expressions found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_expression(slug: str) -> str:
    """Get detailed information about a specific expression.

    Args:
        slug: URL slug identifier for the expression.
    """
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        data = api.get_expression(slug)
        return str(data)


@mcp.tool()
def list_distilleries(limit: int = 20, offset: int = 0) -> str:
    """List distilleries from whiskeyfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        data = api.list_distilleries(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No distilleries found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_whiskey(query: str) -> str:
    """Search whiskeyfyi.com for whiskey expressions, distilleries, and regions.

    Args:
        query: Search query string.
    """
    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
