import pytest


@pytest.mark.asyncio
async def test_get_activities_contains_known_activity(async_client):
    # Arrange: async_client fixture

    # Act
    resp = await async_client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()

    # Assert
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
