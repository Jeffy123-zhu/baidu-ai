import pytest
from src.web.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test main page loads"""
    response = client.get('/')
    assert response.status_code == 200


def test_status_endpoint(client):
    """Test status API"""
    response = client.get('/api/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['service'] == 'MediDoc AI'
    assert data['status'] == 'running'


def test_upload_no_file(client):
    """Test upload without file"""
    response = client.post('/api/upload')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_diagnose_endpoint(client):
    """Test diagnose API"""
    response = client.post('/api/diagnose',
                          json={'document': 'test'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'diagnosis' in data
