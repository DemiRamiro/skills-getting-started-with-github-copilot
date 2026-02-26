import pytest


@pytest.mark.asyncio
async def test_root_redirect(async_client):
    # Arrange: async_client fixture
    # Act
    resp = await async_client.get("/")

    # Assert
    assert resp.status_code in (307, 308)
    assert resp.headers.get("location", "").endswith("/static/index.html")
