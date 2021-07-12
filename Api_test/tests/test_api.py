import pytest
from api import app as flask_app
from flask import json


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


class TestApi:
    def test_ping(app, client):
        res = client.get('/api/ping')
        assert res.status_code == 200
        expected = {'success': True}
        assert expected == json.loads(res.get_data(as_text=True))
    def test_post(app,client):
        res = client.get('/api/posts/?tags=tech')
        assert res.status_code == 200
    def test_post_sortBy(app,client):
        res = client.get('/api/posts/?tags=tech&sortBy=likes&direction=asc')
        assert res.status_code == 200
        