# whiskeyfyi

[![PyPI](https://img.shields.io/pypi/v/whiskeyfyi)](https://pypi.org/project/whiskeyfyi/)
[![Python](https://img.shields.io/pypi/pyversions/whiskeyfyi)](https://pypi.org/project/whiskeyfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Whiskey knowledge API client for Python. Search 80 whiskey expressions, distilleries across 7 countries and 13 regions, and whiskey terminology from [WhiskeyFYI](https://whiskeyfyi.com) -- the comprehensive whiskey reference with 150 expert guides covering single malts, bourbons, cask types, and tasting methodology.

> **Explore whiskey at [whiskeyfyi.com](https://whiskeyfyi.com)** -- [Whiskey Directory](https://whiskeyfyi.com/whiskeys/) | [Distilleries](https://whiskeyfyi.com/distilleries/) | [Regions](https://whiskeyfyi.com/regions/) | [Whiskey Guides](https://whiskeyfyi.com/guides/)

<p align="center">
  <img src="demo.gif" alt="whiskeyfyi demo -- whiskey API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on WhiskeyFYI](#what-youll-find-on-whiskeyfyi)
  - [Whiskey Types](#whiskey-types)
  - [Cask Types and Maturation](#cask-types-and-maturation)
  - [Whiskey Regions](#whiskey-regions)
  - [Key Whiskey Terms](#key-whiskey-terms)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Whiskey](#learn-more-about-whiskey)
- [Beverage FYI Family](#beverage-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

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
    # Search whiskey expressions, distilleries, glossary terms
    results = api.search("bourbon")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("cask-strength")
    print(term["definition"])
```

## What You'll Find on WhiskeyFYI

WhiskeyFYI is a comprehensive whiskey reference covering 80 whiskey expressions, distilleries across 7 countries and 13 regions, and 150 expert guides. The database spans the world of whiskey -- from Scotch single malts and Kentucky bourbon to Japanese whisky and Irish pot still traditions.

### Whiskey Types

Whiskey classification is governed by legal definitions that vary by country. Each type has strict production requirements covering grain bill, distillation method, aging duration, and cask type:

| Type | Country | Key Requirements |
|------|---------|-----------------|
| Scotch Single Malt | Scotland | 100% malted barley, pot still, 3+ years in oak, single distillery |
| Scotch Blended | Scotland | Mix of malt and grain whiskies from multiple distilleries |
| Bourbon | United States | 51%+ corn, new charred oak barrels, max 62.5% ABV entry |
| Tennessee | United States | Bourbon requirements + Lincoln County Process (charcoal filtering) |
| Rye (American) | United States | 51%+ rye grain, new charred oak barrels |
| Irish Whiskey | Ireland | 3+ years aging, pot still or column still, triple distillation common |
| Japanese Whisky | Japan | Scotch-influenced, single malt and blended styles |
| Canadian | Canada | 3+ years aging, often rye-forward blends, allows flavoring |

Learn more: [Browse Whiskey Types](https://whiskeyfyi.com/type/) · [Whiskey Encyclopedia](https://whiskeyfyi.com/whiskey/)

### Cask Types and Maturation

Maturation accounts for an estimated 60-80% of a whiskey's final flavor. The cask type, previous contents, size, and number of uses all shape the spirit's character:

| Cask Type | Capacity | Flavor Contribution |
|-----------|----------|---------------------|
| Ex-Bourbon (American Oak) | 200L | Vanilla, caramel, coconut, sweet spice |
| Sherry (Oloroso) | 500L | Dried fruit, nuts, chocolate, rich sweetness |
| Sherry (Pedro Ximenez) | 500L | Intense sweetness, raisins, dark chocolate |
| Port | 500L | Berry fruit, plum, wine-like sweetness |
| Virgin Oak (New Charred) | 200L | Strong oak, tannins, char, spice |
| Rum | 200L | Tropical fruit, molasses, brown sugar |
| Wine (Red/White) | 225L | Fruit character, tannic structure, acidity |
| Mizunara (Japanese Oak) | 480L | Sandalwood, incense, coconut, rare and costly |

First-fill casks impart the most flavor, with each subsequent use ("refill") contributing progressively less. Cask strength bottlings (typically 55-65% ABV) are not diluted after maturation, preserving the full intensity of the spirit.

Learn more: [Cask Types Guide](https://whiskeyfyi.com/cask/) · [Whiskey Glossary](https://whiskeyfyi.com/glossary/)

### Whiskey Regions

Each whiskey-producing region has distinctive characteristics shaped by climate, water sources, grain availability, and local traditions:

| Region | Country | Characteristics |
|--------|---------|-----------------|
| Speyside | Scotland | Elegant, fruity, honeyed, often sherry-matured |
| Islay | Scotland | Heavily peated, maritime, medicinal, smoky |
| Highland | Scotland | Diverse, from light floral to robust and peaty |
| Lowland | Scotland | Light, grassy, gentle, triple distillation |
| Campbeltown | Scotland | Briny, slightly smoky, oily, complex |
| Kentucky | USA | Bourbon heartland, limestone water, corn-forward |
| Cooley/Midleton | Ireland | Pot still tradition, smooth, triple distilled |
| Yamazaki/Hakushu | Japan | Precision crafting, varied yeast strains, multiple still types |

Learn more: [Explore 13 Whiskey Regions](https://whiskeyfyi.com/region/) · [Country Profiles](https://whiskeyfyi.com/country/)

### Key Whiskey Terms

| Term | Definition |
|------|-----------|
| Age Statement | Minimum years the youngest whiskey in a bottle has been aged |
| Cask Strength | Bottled at barrel proof without water dilution |
| Single Cask | Contents of one individual barrel, each unique |
| Peat | Decomposed vegetation burned during malting, imparts smoky phenols |
| Angel's Share | Portion lost to evaporation during aging (1-2% per year) |
| Non-Chill Filtered | Skips cold filtration, retains oils and texture |
| Phenol (PPM) | Parts per million, measures peat smoke intensity |

Learn more: [Flavor Profiles](https://whiskeyfyi.com/flavor/) · [Whiskey Guides](https://whiskeyfyi.com/guide/)

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/whiskeys/` | List all 80 whiskey expressions |
| GET | `/api/v1/whiskeys/{slug}/` | Whiskey detail with tasting notes |
| GET | `/api/v1/distilleries/` | List distilleries |
| GET | `/api/v1/distilleries/{slug}/` | Distillery detail with history |
| GET | `/api/v1/regions/` | List all 13 whiskey regions |
| GET | `/api/v1/regions/{slug}/` | Region detail with characteristics |
| GET | `/api/v1/glossary/` | List all whiskey terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two whiskeys |
| GET | `/api/v1/random/` | Random whiskey expression |
| GET | `/api/v1/guides/` | List all 150 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://whiskeyfyi.com/api/v1/whiskeys/lagavulin-16/"
```

```json
{
  "slug": "lagavulin-16",
  "name": "Lagavulin 16 Year Old",
  "type": "Single Malt Scotch",
  "region": "Islay",
  "country": "Scotland",
  "age_statement": 16,
  "abv": 43.0,
  "cask_type": "ex-bourbon and sherry",
  "description": "Iconic Islay single malt known for its intense peat smoke balanced with rich sweetness and maritime character.",
  "tasting_notes": {
    "nose": ["peat smoke", "iodine", "seaweed", "dried fruit"],
    "palate": ["rich smoke", "malt sweetness", "sherry", "oak"],
    "finish": ["long", "smoky", "warming", "dry"]
  },
  "url": "https://whiskeyfyi.com/whiskeys/lagavulin-16/"
}
```

Full API documentation: [whiskeyfyi.com/developers/](https://whiskeyfyi.com/developers/).
OpenAPI 3.1.0 spec: [whiskeyfyi.com/api/v1/openapi.json](https://whiskeyfyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search whiskeys, distilleries, regions
whiskeyfyi search "bourbon"
whiskeyfyi search "Lagavulin"
whiskeyfyi search "single malt"
whiskeyfyi search "islay"

# Look up whiskey terminology
whiskeyfyi term "cask-strength"
whiskeyfyi term "angels-share"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted whiskey queries:

```bash
python -m whiskeyfyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "whiskeyfyi": {
      "command": "uvx",
      "args": ["--from", "whiskeyfyi[mcp]", "python", "-m", "whiskeyfyi.mcp_server"]
    }
  }
}
```

**Tools**: `whiskey_search`, `whiskey_glossary_term`

## API Client

```python
from whiskeyfyi.api import WhiskeyFYI

with WhiskeyFYI() as api:
    # Search across whiskeys, distilleries, regions, glossary
    results = api.search("scotch")

    # Look up whiskey terminology
    term = api.glossary_term("non-chill-filtered")
    print(term["definition"])

    # Compare two whiskeys
    comparison = api.compare("lagavulin-16", "laphroaig-10")

    # Get a random whiskey
    random_whiskey = api.random()
```

## Learn More About Whiskey

- **Reference**: [Whiskey Directory](https://whiskeyfyi.com/whiskeys/) | [Distilleries](https://whiskeyfyi.com/distilleries/) | [Regions](https://whiskeyfyi.com/regions/)
- **Glossary**: [Whiskey Terminology](https://whiskeyfyi.com/glossary/)
- **Guides**: [Whiskey Guides](https://whiskeyfyi.com/guides/)
- **Compare**: [Whiskey Comparisons](https://whiskeyfyi.com/compare/)
- **API**: [Developer Docs](https://whiskeyfyi.com/developers/) | [OpenAPI Spec](https://whiskeyfyi.com/api/v1/openapi.json)

## Beverage FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktail recipes, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, brewing guides |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| **WhiskeyFYI** | [whiskeyfyi.com](https://whiskeyfyi.com) | **80 whiskey expressions, distilleries, regions** |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis -- [emojifyi.com](https://emojifyi.com) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com) |
| vinofyi | [PyPI](https://pypi.org/project/vinofyi/) | -- | Wine API client -- grapes, regions, wineries -- [vinofyi.com](https://vinofyi.com) |
| beerfyi | [PyPI](https://pypi.org/project/beerfyi/) | -- | Beer styles, hops, malts API -- [beerfyi.com](https://beerfyi.com) |
| brewfyi | [PyPI](https://pypi.org/project/brewfyi/) | -- | Coffee varieties, brew methods API -- [brewfyi.com](https://brewfyi.com) |
| **whiskeyfyi** | [PyPI](https://pypi.org/project/whiskeyfyi/) | -- | **Whiskey expressions, distilleries API -- [whiskeyfyi.com](https://whiskeyfyi.com)** |
| teafyi | [PyPI](https://pypi.org/project/teafyi/) | -- | Tea varieties, teaware API -- [teafyi.com](https://teafyi.com) |
| nihonshufyi | [PyPI](https://pypi.org/project/nihonshufyi/) | -- | Sake grades, breweries API -- [nihonshufyi.com](https://nihonshufyi.com) |
| drinkfyi | [PyPI](https://pypi.org/project/drinkfyi/) | -- | Unified beverage hub -- 7 sites -- [fyipedia.com](https://fyipedia.com) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI: `fyi color info FF6B35` -- [fyipedia.com](https://fyipedia.com) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP hub for AI assistants -- [fyipedia.com](https://fyipedia.com) |

## License

MIT
