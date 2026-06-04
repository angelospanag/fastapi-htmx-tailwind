from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    with TestClient(app) as c:
        yield c


def test_index(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert "text/html" in response.headers["content-type"]


def test_tab1(client):
    response = client.get("/tab1")
    assert response.status_code == HTTPStatus.OK
    assert "text/html" in response.headers["content-type"]


def test_tab2(client):
    response = client.get("/tab2")
    assert response.status_code == HTTPStatus.OK
    assert "text/html" in response.headers["content-type"]


def test_tab3(client):
    response = client.get("/tab3")
    assert response.status_code == HTTPStatus.OK
    assert "text/html" in response.headers["content-type"]
