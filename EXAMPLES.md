# VitalApp Backend - API Examples

This document provides practical examples of how to use the VitalApp Backend API.

## Base URL

- **Local Development**: `http://localhost:8000`
- **API Prefix**: `/api/v1`

## Health Check

### Check API Health

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "app_name": "VitalApp Backend",
  "version": "1.0.0"
}
```

## Pacientes (Patients)

### Create a Patient

```bash
curl -X POST http://localhost:8000/api/v1/pacientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@example.com",
    "telefono": "+1234567890",
    "fecha_nacimiento": "1990-01-15",
    "direccion": "Calle Principal 123, Ciudad"
  }'
```

**Response:**
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan.perez@example.com",
  "telefono": "+1234567890",
  "fecha_nacimiento": "1990-01-15",
  "direccion": "Calle Principal 123, Ciudad",
  "created_at": "2024-01-20T10:30:00.000Z",
  "updated_at": null
}
```

### Get All Patients

```bash
curl http://localhost:8000/api/v1/pacientes/
```

**With pagination:**
```bash
curl "http://localhost:8000/api/v1/pacientes/?skip=0&limit=10"
```

### Get Patient by ID

```bash
curl http://localhost:8000/api/v1/pacientes/1
```

### Update a Patient

```bash
curl -X PUT http://localhost:8000/api/v1/pacientes/1 \
  -H "Content-Type: application/json" \
  -d '{
    "telefono": "+0987654321",
    "direccion": "Nueva Dirección 456"
  }'
```

### Delete a Patient

```bash
curl -X DELETE http://localhost:8000/api/v1/pacientes/1
```

## Citas (Appointments)

### Create an Appointment

```bash
curl -X POST http://localhost:8000/api/v1/citas/ \
  -H "Content-Type: application/json" \
  -d '{
    "paciente_id": 1,
    "fecha_hora": "2024-02-15T14:30:00",
    "motivo": "Consulta general",
    "estado": "programada",
    "notas": "Primera consulta del paciente"
  }'
```

**Response:**
```json
{
  "id": 1,
  "paciente_id": 1,
  "fecha_hora": "2024-02-15T14:30:00",
  "motivo": "Consulta general",
  "estado": "programada",
  "notas": "Primera consulta del paciente",
  "created_at": "2024-01-20T10:35:00.000Z",
  "updated_at": null
}
```

### Get All Appointments

```bash
curl http://localhost:8000/api/v1/citas/
```

### Get Appointments by Patient

```bash
curl http://localhost:8000/api/v1/citas/paciente/1
```

### Get Appointment by ID

```bash
curl http://localhost:8000/api/v1/citas/1
```

### Update an Appointment

```bash
curl -X PUT http://localhost:8000/api/v1/citas/1 \
  -H "Content-Type: application/json" \
  -d '{
    "estado": "confirmada",
    "notas": "Paciente confirmó asistencia"
  }'
```

### Cancel an Appointment

```bash
curl -X PUT http://localhost:8000/api/v1/citas/1 \
  -H "Content-Type: application/json" \
  -d '{
    "estado": "cancelada",
    "notas": "Cancelada por el paciente"
  }'
```

### Delete an Appointment

```bash
curl -X DELETE http://localhost:8000/api/v1/citas/1
```

## Resultados (Medical Results)

### Create a Medical Result

```bash
curl -X POST http://localhost:8000/api/v1/resultados/ \
  -H "Content-Type: application/json" \
  -d '{
    "paciente_id": 1,
    "tipo_examen": "Análisis de sangre completo",
    "fecha_examen": "2024-01-20T09:00:00",
    "resultado": "Todos los valores dentro del rango normal",
    "observaciones": "Hemoglobina: 14.5 g/dL, Leucocitos: 7000/μL"
  }'
```

**Response:**
```json
{
  "id": 1,
  "paciente_id": 1,
  "tipo_examen": "Análisis de sangre completo",
  "fecha_examen": "2024-01-20T09:00:00",
  "resultado": "Todos los valores dentro del rango normal",
  "observaciones": "Hemoglobina: 14.5 g/dL, Leucocitos: 7000/μL",
  "created_at": "2024-01-20T10:40:00.000Z",
  "updated_at": null
}
```

### Get All Results

```bash
curl http://localhost:8000/api/v1/resultados/
```

### Get Results by Patient

```bash
curl http://localhost:8000/api/v1/resultados/paciente/1
```

### Get Result by ID

```bash
curl http://localhost:8000/api/v1/resultados/1
```

### Update a Result

```bash
curl -X PUT http://localhost:8000/api/v1/resultados/1 \
  -H "Content-Type: application/json" \
  -d '{
    "observaciones": "Valores normales. Se recomienda control en 6 meses."
  }'
```

### Delete a Result

```bash
curl -X DELETE http://localhost:8000/api/v1/resultados/1
```

## Python Examples

### Using `requests` library

```python
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api/v1"

# Create a patient
patient_data = {
    "nombre": "María",
    "apellido": "García",
    "email": "maria.garcia@example.com",
    "telefono": "+1234567890",
    "fecha_nacimiento": "1985-03-20"
}

response = requests.post(f"{API_URL}/pacientes/", json=patient_data)
patient = response.json()
print(f"Created patient: {patient['id']}")

# Create an appointment for the patient
appointment_data = {
    "paciente_id": patient['id'],
    "fecha_hora": datetime.now().isoformat(),
    "motivo": "Consulta de seguimiento",
    "estado": "programada"
}

response = requests.post(f"{API_URL}/citas/", json=appointment_data)
appointment = response.json()
print(f"Created appointment: {appointment['id']}")

# Get all appointments for the patient
response = requests.get(f"{API_URL}/citas/paciente/{patient['id']}")
appointments = response.json()
print(f"Patient has {len(appointments)} appointments")

# Create a medical result
result_data = {
    "paciente_id": patient['id'],
    "tipo_examen": "Rayos X de tórax",
    "fecha_examen": datetime.now().isoformat(),
    "resultado": "Sin hallazgos patológicos",
    "observaciones": "Campos pulmonares limpios"
}

response = requests.post(f"{API_URL}/resultados/", json=result_data)
result = response.json()
print(f"Created result: {result['id']}")
```

### Using `httpx` library (async)

```python
import httpx
import asyncio
from datetime import datetime

async def main():
    BASE_URL = "http://localhost:8000"
    API_URL = f"{BASE_URL}/api/v1"
    
    async with httpx.AsyncClient() as client:
        # Create a patient
        patient_data = {
            "nombre": "Carlos",
            "apellido": "López",
            "email": "carlos.lopez@example.com"
        }
        
        response = await client.post(f"{API_URL}/pacientes/", json=patient_data)
        patient = response.json()
        print(f"Created patient: {patient['id']}")
        
        # Get all patients
        response = await client.get(f"{API_URL}/pacientes/")
        patients = response.json()
        print(f"Total patients: {len(patients)}")

asyncio.run(main())
```

## JavaScript/TypeScript Examples

### Using `fetch` API

```javascript
const BASE_URL = 'http://localhost:8000';
const API_URL = `${BASE_URL}/api/v1`;

// Create a patient
async function createPatient() {
  const patientData = {
    nombre: 'Ana',
    apellido: 'Martínez',
    email: 'ana.martinez@example.com',
    telefono: '+1234567890',
    fecha_nacimiento: '1992-07-10'
  };

  const response = await fetch(`${API_URL}/pacientes/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(patientData),
  });

  const patient = await response.json();
  console.log('Created patient:', patient.id);
  return patient;
}

// Get all patients
async function getPatients() {
  const response = await fetch(`${API_URL}/pacientes/`);
  const patients = await response.json();
  console.log('Patients:', patients);
  return patients;
}

// Update a patient
async function updatePatient(patientId, updates) {
  const response = await fetch(`${API_URL}/pacientes/${patientId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(updates),
  });

  const patient = await response.json();
  console.log('Updated patient:', patient);
  return patient;
}

// Example usage
(async () => {
  const patient = await createPatient();
  await updatePatient(patient.id, { telefono: '+9876543210' });
  const allPatients = await getPatients();
})();
```

### Using `axios`

```javascript
const axios = require('axios');

const API_URL = 'http://localhost:8000/api/v1';

// Create a patient
axios.post(`${API_URL}/pacientes/`, {
  nombre: 'Pedro',
  apellido: 'Sánchez',
  email: 'pedro.sanchez@example.com'
})
.then(response => {
  console.log('Created patient:', response.data);
})
.catch(error => {
  console.error('Error:', error.response.data);
});

// Get all appointments
axios.get(`${API_URL}/citas/`)
.then(response => {
  console.log('Appointments:', response.data);
})
.catch(error => {
  console.error('Error:', error);
});
```

## Error Handling

### Common HTTP Status Codes

- **200 OK**: Request successful
- **201 Created**: Resource created successfully
- **204 No Content**: Resource deleted successfully
- **400 Bad Request**: Invalid request data
- **404 Not Found**: Resource not found
- **422 Unprocessable Entity**: Validation error

### Example Error Responses

**404 Not Found:**
```json
{
  "detail": "Paciente not found"
}
```

**400 Bad Request (Duplicate email):**
```json
{
  "detail": "Email already registered"
}
```

**422 Validation Error:**
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

## Interactive Documentation

For interactive API documentation with all available endpoints and schemas, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These interfaces allow you to:
- View all available endpoints
- See request/response schemas
- Test endpoints directly from the browser
- Download OpenAPI specification

## Best Practices

1. **Always validate data** before sending requests
2. **Handle errors gracefully** in your application
3. **Use pagination** for large datasets
4. **Store patient IDs** for future operations
5. **Include proper error handling** for network issues
6. **Use environment variables** for API URLs
7. **Implement retry logic** for transient failures
8. **Log API responses** for debugging

## Rate Limiting

Currently, there is no rate limiting implemented. For production use, consider adding:
- Rate limiting middleware
- API key authentication
- Request throttling

## Next Steps

- Implement authentication with Supabase Auth
- Add file upload for medical documents
- Create real-time notifications
- Add search and filtering capabilities
- Implement audit logs

For more information, see:
- [README.md](README.md) - General documentation
- [STEPS.md](STEPS.md) - Setup and deployment guide
