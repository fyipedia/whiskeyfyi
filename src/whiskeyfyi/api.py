"""HTTP API client for whiskeyfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install whiskeyfyi[api]``

Usage::

    from whiskeyfyi.api import WhiskeyFYI

    with WhiskeyFYI() as api:
        items = api.list_casks()
        detail = api.get_cask("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class WhiskeyFYI:
    """API client for the whiskeyfyi.com REST API.

    Provides typed access to all whiskeyfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://whiskeyfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://whiskeyfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_casks(self, **params: Any) -> dict[str, Any]:
        """List all casks."""
        return self._get("/api/v1/casks/", **params)

    def get_cask(self, slug: str) -> dict[str, Any]:
        """Get cask by slug."""
        return self._get(f"/api/v1/casks/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_distilleries(self, **params: Any) -> dict[str, Any]:
        """List all distilleries."""
        return self._get("/api/v1/distilleries/", **params)

    def get_distillery(self, slug: str) -> dict[str, Any]:
        """Get distillery by slug."""
        return self._get(f"/api/v1/distilleries/" + slug + "/")

    def list_expressions(self, **params: Any) -> dict[str, Any]:
        """List all expressions."""
        return self._get("/api/v1/expressions/", **params)

    def get_expression(self, slug: str) -> dict[str, Any]:
        """Get expression by slug."""
        return self._get(f"/api/v1/expressions/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_types(self, **params: Any) -> dict[str, Any]:
        """List all types."""
        return self._get("/api/v1/types/", **params)

    def get_type(self, slug: str) -> dict[str, Any]:
        """Get type by slug."""
        return self._get(f"/api/v1/types/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> WhiskeyFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
