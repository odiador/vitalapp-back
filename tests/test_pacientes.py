import pytest


def test_create_paciente(client):
    """Test creating a paciente"""
    paciente_data = {
        "nombre": "Juan",
        "apellido": "Pérez",
        "email": "juan.perez@example.com",
        "telefono": "+1234567890",
        "fecha_nacimiento": "1990-01-01",
        "direccion": "Calle 123"
    }
    response = client.post("/api/v1/pacientes/", json=paciente_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == paciente_data["nombre"]
    assert data["apellido"] == paciente_data["apellido"]
    assert data["email"] == paciente_data["email"]
    assert "id" in data
    assert "created_at" in data


def test_get_pacientes(client):
    """Test getting all pacientes"""
    # Create a paciente first
    paciente_data = {
        "nombre": "María",
        "apellido": "García",
        "email": "maria.garcia@example.com"
    }
    client.post("/api/v1/pacientes/", json=paciente_data)
    
    # Get all pacientes
    response = client.get("/api/v1/pacientes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_paciente_by_id(client):
    """Test getting a paciente by ID"""
    # Create a paciente first
    paciente_data = {
        "nombre": "Carlos",
        "apellido": "López",
        "email": "carlos.lopez@example.com"
    }
    create_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = create_response.json()["id"]
    
    # Get the paciente
    response = client.get(f"/api/v1/pacientes/{paciente_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == paciente_id
    assert data["nombre"] == paciente_data["nombre"]


def test_update_paciente(client):
    """Test updating a paciente"""
    # Create a paciente first
    paciente_data = {
        "nombre": "Ana",
        "apellido": "Martínez",
        "email": "ana.martinez@example.com"
    }
    create_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = create_response.json()["id"]
    
    # Update the paciente
    update_data = {"telefono": "+9876543210"}
    response = client.put(f"/api/v1/pacientes/{paciente_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["telefono"] == update_data["telefono"]


def test_delete_paciente(client):
    """Test deleting a paciente"""
    # Create a paciente first
    paciente_data = {
        "nombre": "Pedro",
        "apellido": "Rodríguez",
        "email": "pedro.rodriguez@example.com"
    }
    create_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = create_response.json()["id"]
    
    # Delete the paciente
    response = client.delete(f"/api/v1/pacientes/{paciente_id}")
    assert response.status_code == 204
    
    # Verify deletion
    get_response = client.get(f"/api/v1/pacientes/{paciente_id}")
    assert get_response.status_code == 404


def test_create_duplicate_email(client):
    """Test creating a paciente with duplicate email"""
    paciente_data = {
        "nombre": "Luis",
        "apellido": "Hernández",
        "email": "duplicate@example.com"
    }
    # Create first paciente
    client.post("/api/v1/pacientes/", json=paciente_data)
    
    # Try to create duplicate
    response = client.post("/api/v1/pacientes/", json=paciente_data)
    assert response.status_code == 400
