"""whiskeyfyi — Whiskey knowledge API client for developers.

Search whiskey types, distilleries, and terminology from WhiskeyFYI.

Usage::

    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        results = api.search("bourbon")
        print(results)
"""

__version__ = "0.1.0"
