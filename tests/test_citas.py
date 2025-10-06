import pytest
from datetime import datetime, timedelta


def test_create_cita(client):
    """Test creating a cita"""
    # Create a paciente first
    paciente_data = {
        "nombre": "Test",
        "apellido": "User",
        "email": "test.cita@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    # Create a cita
    cita_data = {
        "paciente_id": paciente_id,
        "fecha_hora": (datetime.now() + timedelta(days=1)).isoformat(),
        "motivo": "Consulta general",
        "estado": "programada"
    }
    response = client.post("/api/v1/citas/", json=cita_data)
    assert response.status_code == 201
    data = response.json()
    assert data["paciente_id"] == paciente_id
    assert data["motivo"] == cita_data["motivo"]
    assert "id" in data


def test_get_citas(client):
    """Test getting all citas"""
    # Create a paciente and cita first
    paciente_data = {
        "nombre": "Test2",
        "apellido": "User2",
        "email": "test2.cita@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    cita_data = {
        "paciente_id": paciente_id,
        "fecha_hora": (datetime.now() + timedelta(days=2)).isoformat(),
        "motivo": "Chequeo"
    }
    client.post("/api/v1/citas/", json=cita_data)
    
    # Get all citas
    response = client.get("/api/v1/citas/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_citas_by_paciente(client):
    """Test getting citas for a specific paciente"""
    # Create a paciente and cita first
    paciente_data = {
        "nombre": "Test3",
        "apellido": "User3",
        "email": "test3.cita@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    cita_data = {
        "paciente_id": paciente_id,
        "fecha_hora": (datetime.now() + timedelta(days=3)).isoformat(),
        "motivo": "Seguimiento"
    }
    client.post("/api/v1/citas/", json=cita_data)
    
    # Get citas by paciente
    response = client.get(f"/api/v1/citas/paciente/{paciente_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(cita["paciente_id"] == paciente_id for cita in data)


def test_update_cita(client):
    """Test updating a cita"""
    # Create a paciente and cita first
    paciente_data = {
        "nombre": "Test4",
        "apellido": "User4",
        "email": "test4.cita@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    cita_data = {
        "paciente_id": paciente_id,
        "fecha_hora": (datetime.now() + timedelta(days=4)).isoformat(),
        "motivo": "Inicial"
    }
    cita_response = client.post("/api/v1/citas/", json=cita_data)
    cita_id = cita_response.json()["id"]
    
    # Update the cita
    update_data = {"estado": "confirmada"}
    response = client.put(f"/api/v1/citas/{cita_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["estado"] == "confirmada"


def test_delete_cita(client):
    """Test deleting a cita"""
    # Create a paciente and cita first
    paciente_data = {
        "nombre": "Test5",
        "apellido": "User5",
        "email": "test5.cita@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    cita_data = {
        "paciente_id": paciente_id,
        "fecha_hora": (datetime.now() + timedelta(days=5)).isoformat(),
        "motivo": "Delete test"
    }
    cita_response = client.post("/api/v1/citas/", json=cita_data)
    cita_id = cita_response.json()["id"]
    
    # Delete the cita
    response = client.delete(f"/api/v1/citas/{cita_id}")
    assert response.status_code == 204
    
    # Verify deletion
    get_response = client.get(f"/api/v1/citas/{cita_id}")
    assert get_response.status_code == 404
