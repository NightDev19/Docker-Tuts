import os

os.environ["MONGODB_CONNECTION_STRING"] = (
    "mongodb://root:example@localhost:27017/todolist?authSource=admin"
)

import pytest
from httpx import AsyncClient, ASGITransport

from mysite.main import app


@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}