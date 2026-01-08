import pytest
from app import app, db
from models import Hero, Power, HeroPower

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_heroes(client):
    # Test GET /heroes
    response = client.get('/heroes')
    assert response.status_code == 200
    # Add more assertions based on your API implementation

def test_get_hero_by_id(client):
    # Test GET /heroes/<id>
    response = client.get('/heroes/1')
    assert response.status_code == 200
    # Add more assertions

def test_get_powers(client):
    # Test GET /powers
    response = client.get('/powers')
    assert response.status_code == 200
    # Add more assertions

def test_create_hero_power(client):
    # Test POST /hero_powers
    data = {
        'strength': 'Strong',
        'hero_id': 1,
        'power_id': 1
    }
    response = client.post('/hero_powers', json=data)
    assert response.status_code == 201
    # Add more assertions


