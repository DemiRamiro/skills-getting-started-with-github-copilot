import pytest
from urllib.parse import quote


@pytest.mark.asyncio
async def test_unregister_and_missing(async_client):
    # Arrange
    activity = "Chess Club"
    email = "unreg-tester@example.com"

    # Ensure participant exists by signing up
    resp = await async_client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert resp.status_code == 200

    # Act: unregister
    resp = await async_client.delete(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Unregistered" in resp.json().get("message", "")

    # Verify removed
    resp = await async_client.get("/activities")
    assert email not in resp.json()[activity]["participants"]

    # Act: try removing again (should 404)
    resp = await async_client.delete(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert resp.status_code == 404
