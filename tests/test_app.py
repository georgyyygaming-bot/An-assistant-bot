import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_no_message(client):
    rv = client.post('/chat', json={})
    assert rv.status_code == 400
    assert b'no message' in rv.data

# This test assumes DEEPSEEK_API_KEY is not set; we expect 500

def test_no_api_key(client):
    os.environ.pop('DEEPSEEK_API_KEY', None)
    rv = client.post('/chat', json={'message': 'hi'})
    assert rv.status_code == 500
