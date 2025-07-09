import pytest
from httpx import AsyncClient
from fastapi import status
from run_products_api import app  # Replace with actual module if different

@pytest.mark.asyncio
async def test_missing_query_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
        assert response.status_code == 422  # FastAPI will auto return 422
        assert "detail" in response.json()

@pytest.mark.asyncio
async def test_missing_query_outlets():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/outlets/")
        assert response.status_code == 422
        assert "detail" in response.json()

@pytest.mark.asyncio
async def test_malicious_input():
    malicious_input = "'; DROP TABLE users;--"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/outlets/?query={malicious_input}")
        assert response.status_code == 200
        assert "You asked about" in response.json()["result"]  # No crash, just echo

@pytest.mark.asyncio
async def test_api_downtime_simulation(monkeypatch):
    from app.api.outlets import search_outlets

    def fake_fail(*args, **kwargs):
        raise Exception("Simulated backend failure")

    monkeypatch.setattr("app.api.outlets.search_outlets", fake_fail)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/outlets/?query=open after 9pm")
        assert response.status_code == 500
        assert "Internal Server Error" in response.text
