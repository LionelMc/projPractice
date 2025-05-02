from fastapi.testclient import TestClient
from app import app  # Importa la instancia de la aplicación

client = TestClient(app)

def test_get_familia():
    response = client.get("/familia")
    assert response.status_code == 200
    assert response.json() == ["Amin", "Marce", "Miranda"]

def test_get_superheroes_dc():
    response = client.get("/superheroesDC")
    assert response.status_code == 200
    assert "Superman" in response.json()

def test_get_superheroes_marvel():
    response = client.get("/superheroesMarvel")
    assert response.status_code == 200
    assert "Spiderman" in response.json()

def test_get_cursos_platzi():
    response = client.get("/cursosPlatzi")
    assert response.status_code == 200
    assert "Python" in response.json()