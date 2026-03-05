"""Tests for whiskeyfyi.api — client initialization and URL construction."""

from whiskeyfyi.api import WhiskeyFYI


class TestWhiskeyFYIInit:
    def test_default_base_url(self) -> None:
        client = WhiskeyFYI()
        assert str(client._client.base_url) == "https://whiskeyfyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = WhiskeyFYI(base_url="https://test.whiskeyfyi.com")
        assert str(client._client.base_url) == "https://test.whiskeyfyi.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = WhiskeyFYI()
        assert client._client.timeout.connect == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = WhiskeyFYI(timeout=30.0)
        assert client._client.timeout.connect == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with WhiskeyFYI() as client:
            assert str(client._client.base_url) == "https://whiskeyfyi.com"


class TestWhiskeyFYIVersion:
    def test_version(self) -> None:
        from whiskeyfyi import __version__

        assert __version__ == "0.1.0"
