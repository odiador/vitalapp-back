import pytest
from datetime import datetime, timedelta


def test_create_resultado(client):
    """Test creating a resultado"""
    # Create a paciente first
    paciente_data = {
        "nombre": "Test",
        "apellido": "Resultado",
        "email": "test.resultado@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    # Create a resultado
    resultado_data = {
        "paciente_id": paciente_id,
        "tipo_examen": "Análisis de sangre",
        "fecha_examen": datetime.now().isoformat(),
        "resultado": "Normal",
        "observaciones": "Todo en orden"
    }
    response = client.post("/api/v1/resultados/", json=resultado_data)
    assert response.status_code == 201
    data = response.json()
    assert data["paciente_id"] == paciente_id
    assert data["tipo_examen"] == resultado_data["tipo_examen"]
    assert "id" in data


def test_get_resultados(client):
    """Test getting all resultados"""
    # Create a paciente and resultado first
    paciente_data = {
        "nombre": "Test2",
        "apellido": "Resultado2",
        "email": "test2.resultado@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    resultado_data = {
        "paciente_id": paciente_id,
        "tipo_examen": "Rayos X",
        "fecha_examen": datetime.now().isoformat(),
        "resultado": "Sin hallazgos"
    }
    client.post("/api/v1/resultados/", json=resultado_data)
    
    # Get all resultados
    response = client.get("/api/v1/resultados/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_resultados_by_paciente(client):
    """Test getting resultados for a specific paciente"""
    # Create a paciente and resultado first
    paciente_data = {
        "nombre": "Test3",
        "apellido": "Resultado3",
        "email": "test3.resultado@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    resultado_data = {
        "paciente_id": paciente_id,
        "tipo_examen": "Ultrasonido",
        "fecha_examen": datetime.now().isoformat(),
        "resultado": "Normal"
    }
    client.post("/api/v1/resultados/", json=resultado_data)
    
    # Get resultados by paciente
    response = client.get(f"/api/v1/resultados/paciente/{paciente_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(resultado["paciente_id"] == paciente_id for resultado in data)


def test_update_resultado(client):
    """Test updating a resultado"""
    # Create a paciente and resultado first
    paciente_data = {
        "nombre": "Test4",
        "apellido": "Resultado4",
        "email": "test4.resultado@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    resultado_data = {
        "paciente_id": paciente_id,
        "tipo_examen": "EKG",
        "fecha_examen": datetime.now().isoformat(),
        "resultado": "Pendiente"
    }
    resultado_response = client.post("/api/v1/resultados/", json=resultado_data)
    resultado_id = resultado_response.json()["id"]
    
    # Update the resultado
    update_data = {"resultado": "Completado - Normal"}
    response = client.put(f"/api/v1/resultados/{resultado_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["resultado"] == "Completado - Normal"


def test_delete_resultado(client):
    """Test deleting a resultado"""
    # Create a paciente and resultado first
    paciente_data = {
        "nombre": "Test5",
        "apellido": "Resultado5",
        "email": "test5.resultado@example.com"
    }
    paciente_response = client.post("/api/v1/pacientes/", json=paciente_data)
    paciente_id = paciente_response.json()["id"]
    
    resultado_data = {
        "paciente_id": paciente_id,
        "tipo_examen": "Delete test",
        "fecha_examen": datetime.now().isoformat(),
        "resultado": "Test"
    }
    resultado_response = client.post("/api/v1/resultados/", json=resultado_data)
    resultado_id = resultado_response.json()["id"]
    
    # Delete the resultado
    response = client.delete(f"/api/v1/resultados/{resultado_id}")
    assert response.status_code == 204
    
    # Verify deletion
    get_response = client.get(f"/api/v1/resultados/{resultado_id}")
    assert get_response.status_code == 404
