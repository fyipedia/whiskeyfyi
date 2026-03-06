---
name: whiskey-tools
description: Search 80 whiskey expressions, distilleries across 7 countries and 13 regions, and whiskey terminology from WhiskeyFYI. Use when answering questions about whiskey types, cask maturation, distilleries, or tasting notes.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://whiskeyfyi.com/"
---

# WhiskeyFYI -- Whiskey Tools for AI Agents

Whiskey knowledge API client for Python. Search 80 whiskey expressions, distilleries across 7 countries and 13 regions, and whiskey terminology from WhiskeyFYI -- the comprehensive whiskey reference with 150 expert guides covering single malts, bourbons, cask types, and tasting methodology.

**Install**: `pip install whiskeyfyi[api]` -- **Web**: [whiskeyfyi.com](https://whiskeyfyi.com/) -- **API**: [REST API](https://whiskeyfyi.com/developers/) -- **PyPI**: [whiskeyfyi](https://pypi.org/project/whiskeyfyi/)

## When to Use

- User asks about whiskey types, legal definitions, or regional styles
- User needs cask maturation information (bourbon, sherry, port, mizunara)
- User wants distillery profiles or regional characteristics
- User asks about whiskey terminology (cask strength, angel's share, PPM)
- User needs to compare whiskey expressions

## Tools

### `WhiskeyFYI` API Client

HTTP client for the whiskeyfyi.com REST API. Requires `pip install whiskeyfyi[api]`.

```python
from whiskeyfyi.api import WhiskeyFYI

with WhiskeyFYI() as api:
    results = api.search("bourbon")    # Search whiskeys, distilleries, glossary
```

**Methods:**
- `search(query: str) -> dict` -- Search whiskeys, distilleries, and glossary terms

## REST API (No Auth Required)

```bash
# Search
curl "https://whiskeyfyi.com/api/v1/search/?q=bourbon"

# Whiskey detail
curl "https://whiskeyfyi.com/api/v1/whiskeys/lagavulin-16/"

# Distillery detail
curl "https://whiskeyfyi.com/api/v1/distilleries/lagavulin/"

# Glossary term
curl "https://whiskeyfyi.com/api/v1/glossary/cask-strength/"

# Compare two whiskeys
curl "https://whiskeyfyi.com/api/v1/compare/lagavulin-16/laphroaig-10/"
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/whiskeys/` | List all 80 whiskey expressions |
| GET | `/api/v1/whiskeys/{slug}/` | Whiskey detail with tasting notes |
| GET | `/api/v1/distilleries/` | List distilleries |
| GET | `/api/v1/distilleries/{slug}/` | Distillery detail with history |
| GET | `/api/v1/regions/` | List all 13 whiskey regions |
| GET | `/api/v1/regions/{slug}/` | Region detail with characteristics |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two whiskeys |
| GET | `/api/v1/random/` | Random whiskey expression |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://whiskeyfyi.com/api/v1/openapi.json)

## Whiskey Types

| Type | Country | Key Requirements |
|------|---------|-----------------|
| Scotch Single Malt | Scotland | 100% malted barley, pot still, 3+ years in oak |
| Scotch Blended | Scotland | Mix of malt and grain whiskies, multiple distilleries |
| Bourbon | United States | 51%+ corn, new charred oak, max 62.5% ABV entry |
| Tennessee | United States | Bourbon + Lincoln County Process (charcoal filtering) |
| Rye (American) | United States | 51%+ rye grain, new charred oak |
| Irish Whiskey | Ireland | 3+ years aging, triple distillation common |
| Japanese Whisky | Japan | Scotch-influenced, single malt and blended |
| Canadian | Canada | 3+ years aging, rye-forward blends |

## Cask Types

| Cask Type | Capacity | Flavor Contribution |
|-----------|----------|---------------------|
| Ex-Bourbon (American Oak) | 200L | Vanilla, caramel, coconut, sweet spice |
| Sherry (Oloroso) | 500L | Dried fruit, nuts, chocolate, rich sweetness |
| Sherry (Pedro Ximenez) | 500L | Intense sweetness, raisins, dark chocolate |
| Port | 500L | Berry fruit, plum, wine-like sweetness |
| Virgin Oak (New Charred) | 200L | Strong oak, tannins, char, spice |
| Mizunara (Japanese Oak) | 480L | Sandalwood, incense, coconut |

## Whiskey Regions

| Region | Country | Characteristics |
|--------|---------|-----------------|
| Speyside | Scotland | Elegant, fruity, honeyed, sherry-matured |
| Islay | Scotland | Heavily peated, maritime, smoky |
| Highland | Scotland | Diverse, light floral to robust peaty |
| Kentucky | USA | Bourbon heartland, limestone water, corn-forward |
| Yamazaki/Hakushu | Japan | Precision crafting, varied yeast strains |

## Demo

![WhiskeyFYI demo](https://raw.githubusercontent.com/fyipedia/whiskeyfyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
