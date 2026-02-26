import copy

import pytest
import pytest_asyncio
from httpx import AsyncClient

from src.app import app
import src.app as app_module


@pytest_asyncio.fixture
async def async_client():
    """Async HTTP client fixture for in-process ASGI testing."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(autouse=True)
def activities_backup():
    """Backup and restore the in-memory activities dict around each test.

    This prevents tests from interfering with each other's mutations.
    """
    backup = copy.deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities = backup
