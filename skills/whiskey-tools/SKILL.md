---
name: whiskey-tools
description: Search 2,200+ whiskey expressions, 500+ distilleries, 14 types, and 18 cask types with tasting notes and regional classifications.
---

# Whiskey Tools

Whiskey search and reference powered by [whiskeyfyi](https://whiskeyfyi.com/) -- a comprehensive whiskey knowledge platform covering 2,200+ expressions, 500+ distilleries, and 14 whiskey types.

## Setup

Install the MCP server:

```bash
pip install "whiskeyfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "whiskeyfyi": {
            "command": "python",
            "args": ["-m", "whiskeyfyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `whiskey_search` | Search whiskey expressions, distilleries, types, regions, and tasting notes |

## When to Use

- Looking up whiskey expressions and tasting notes
- Researching distilleries by region (Scotland, Ireland, Japan, USA, etc.)
- Understanding whiskey types (Scotch, Bourbon, Rye, Irish, Japanese, etc.)
- Exploring cask types and their influence on flavor
- Finding whiskey recommendations by flavor profile

## Links

- [2,200+ Whiskey Expressions](https://whiskeyfyi.com/whiskeys/)
- [500+ Distilleries](https://whiskeyfyi.com/distilleries/)
- [14 Whiskey Types](https://whiskeyfyi.com/types/)
- [API Documentation](https://whiskeyfyi.com/developers/)
- [PyPI Package](https://pypi.org/project/whiskeyfyi/)
