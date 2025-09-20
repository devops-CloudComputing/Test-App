import os
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_healthz_ok(client):
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_failcheck_ok_by_default(client):
    # default is not failing
    resp = client.get("/failcheck")
    assert resp.status_code == 200

def test_failcheck_can_fail(monkeypatch, client):
    monkeypatch.setenv("FAILCHECK", "true")
    resp = client.get("/failcheck")
    assert resp.status_code == 500
