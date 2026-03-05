# whiskeyfyi

Whiskey knowledge API client for developers — search whiskey types, distilleries, and terminology from [WhiskeyFYI](https://whiskeyfyi.com).

<p align="center">
  <img src="demo.gif" alt="whiskeyfyi demo — whiskey API search and lookup" width="800">
</p>

## Install

```bash
pip install whiskeyfyi[api]     # API client (httpx)
pip install whiskeyfyi[cli]     # + CLI (typer, rich)
pip install whiskeyfyi[mcp]     # + MCP server
pip install whiskeyfyi[all]     # Everything
```

## Quick Start

```python
from whiskeyfyi.api import WhiskeyFYI

with WhiskeyFYI() as api:
    results = api.search("bourbon")
    print(results)
```

## CLI

```bash
whiskeyfyi search "bourbon"
whiskeyfyi search "Lagavulin"
whiskeyfyi search "single malt"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m whiskeyfyi.mcp_server
```

Tools: `whiskey_search`

## API Client

```python
from whiskeyfyi.api import WhiskeyFYI

with WhiskeyFYI() as api:
    # Search whiskeys, distilleries, and terms
    results = api.search("scotch")
```

## Links

- [WhiskeyFYI](https://whiskeyfyi.com) — Whiskey encyclopedia with types, distilleries, and tasting guides
- [PyPI](https://pypi.org/project/whiskeyfyi/)
- [GitHub](https://github.com/fyipedia/whiskeyfyi)
- [FYIPedia](https://fyipedia.com) — Open-source developer tools ecosystem
