import pytest
from urllib.parse import quote


@pytest.mark.asyncio
async def test_signup_and_duplicate(async_client):
    # Arrange
    activity = "Chess Club"
    email = "tester@example.com"

    # Ensure not present initially
    resp = await async_client.get("/activities")
    assert resp.status_code == 200
    assert email not in resp.json()[activity]["participants"]

    # Act: sign up
    resp = await async_client.post(f"/activities/{quote(activity)}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Verify appears in participants
    resp = await async_client.get("/activities")
    assert email in resp.json()[activity]["participants"]

    # Act: duplicate signup
    resp = await async_client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    # Assert duplicate rejected
    assert resp.status_code == 400
