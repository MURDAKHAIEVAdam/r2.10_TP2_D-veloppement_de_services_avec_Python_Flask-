# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    """Crée un client de test Flask pour simuler les requêtes HTTP."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_describe_success_serie_a(client):
    """1. Test du cas idéal avec la série A"""
    response = client.get('/db/stats/describe?serie=serie_A')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['source'] == 'mysql'
    assert data['resultat']['serie'] == 'serie_A'
    assert data['resultat']['moyenne'] == 14.14 

def test_describe_success_serie_b(client):
    """2. Test du cas idéal avec la série B"""
    response = client.get('/db/stats/describe?serie=serie_B')
    assert response.status_code == 200

def test_describe_serie_not_found(client):
    """3. Test d'une série qui n'existe pas en BDD (404)"""
    response = client.get('/db/stats/describe?serie=serie_Inexistante')
    data = response.get_json()
    
    assert response.status_code == 404
    assert 'erreur' in data

def test_describe_missing_parameter(client):
    """4. Test du paramètre manquant dans l'URL (400)"""
    response = client.get('/db/stats/describe')
    data = response.get_json()
    
    assert response.status_code == 400
    assert data['erreur'] == "Paramètre 'serie' manquant"