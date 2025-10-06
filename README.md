# VitalApp Backend

Backend API REST para VitalApp, construido con FastAPI y Supabase. Proporciona una API completa para gestionar pacientes, citas médicas y resultados de exámenes.

## 🚀 Características

- **FastAPI**: Framework web moderno y rápido para construir APIs
- **Supabase**: Base de datos PostgreSQL y autenticación
- **SQLAlchemy**: ORM para interactuar con la base de datos
- **Pydantic**: Validación de datos y serialización
- **Pytest**: Framework de testing completo
- **Docker**: Contenerización para desarrollo y despliegue
- **CRUD completo**: Operaciones Create, Read, Update, Delete para todas las entidades

## 📋 Requisitos Previos

- Python 3.11+
- Docker y Docker Compose (opcional)
- Cuenta de Supabase (para producción)

## 🛠️ Instalación

### Opción 1: Instalación Local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/odiador/vitalapp-back.git
   cd vitalapp-back
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

5. **Ejecutar la aplicación**
   ```bash
   uvicorn app.main:app --reload
   ```

### Opción 2: Con Docker

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/odiador/vitalapp-back.git
   cd vitalapp-back
   ```

2. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

3. **Iniciar con Docker Compose**
   ```bash
   docker-compose up -d
   ```

## 🔧 Configuración

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
SUPABASE_SERVICE_KEY=your-supabase-service-role-key

# Database Configuration
DATABASE_URL=postgresql://postgres:your-password@db.your-project.supabase.co:5432/postgres

# Application Configuration
APP_NAME=VitalApp Backend
APP_VERSION=1.0.0
DEBUG=True

# API Configuration
API_PREFIX=/api/v1
```

### Conectar con Supabase

1. **Crear un proyecto en Supabase**
   - Ve a [supabase.com](https://supabase.com)
   - Crea un nuevo proyecto
   - Espera a que se inicialice

2. **Obtener credenciales**
   - En tu proyecto, ve a Settings > API
   - Copia la `URL` y `anon/public key`
   - Copia la `service_role key` (para operaciones administrativas)

3. **Obtener la URL de la base de datos**
   - Ve a Settings > Database
   - Copia la cadena de conexión (Connection string)
   - Formato: `postgresql://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres`

4. **Configurar el archivo .env**
   - Actualiza las variables con tus credenciales
   - La aplicación creará las tablas automáticamente al iniciar

## 📚 API Endpoints

### Health Check
- `GET /health` - Verificar estado de la API

### Pacientes
- `GET /api/v1/pacientes/` - Obtener todos los pacientes
- `GET /api/v1/pacientes/{id}` - Obtener un paciente por ID
- `POST /api/v1/pacientes/` - Crear un nuevo paciente
- `PUT /api/v1/pacientes/{id}` - Actualizar un paciente
- `DELETE /api/v1/pacientes/{id}` - Eliminar un paciente

### Citas
- `GET /api/v1/citas/` - Obtener todas las citas
- `GET /api/v1/citas/{id}` - Obtener una cita por ID
- `GET /api/v1/citas/paciente/{paciente_id}` - Obtener citas de un paciente
- `POST /api/v1/citas/` - Crear una nueva cita
- `PUT /api/v1/citas/{id}` - Actualizar una cita
- `DELETE /api/v1/citas/{id}` - Eliminar una cita

### Resultados
- `GET /api/v1/resultados/` - Obtener todos los resultados
- `GET /api/v1/resultados/{id}` - Obtener un resultado por ID
- `GET /api/v1/resultados/paciente/{paciente_id}` - Obtener resultados de un paciente
- `POST /api/v1/resultados/` - Crear un nuevo resultado
- `PUT /api/v1/resultados/{id}` - Actualizar un resultado
- `DELETE /api/v1/resultados/{id}` - Eliminar un resultado

## 📖 Documentación API

Una vez que la aplicación esté ejecutándose, puedes acceder a la documentación interactiva:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar tests con cobertura
```bash
pytest --cov=app --cov-report=html
```

### Ejecutar tests específicos
```bash
pytest tests/test_pacientes.py
pytest tests/test_citas.py
pytest tests/test_resultados.py
```

## 🏗️ Estructura del Proyecto

```
vitalapp-back/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación FastAPI principal
│   ├── config.py            # Configuración de la aplicación
│   ├── database.py          # Configuración de base de datos
│   ├── models/              # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── paciente.py
│   │   ├── cita.py
│   │   └── resultado.py
│   ├── schemas/             # Esquemas Pydantic
│   │   ├── __init__.py
│   │   ├── paciente.py
│   │   ├── cita.py
│   │   └── resultado.py
│   ├── routers/             # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── pacientes.py
│   │   ├── citas.py
│   │   └── resultados.py
│   └── services/            # Lógica de negocio y CRUD
│       ├── __init__.py
│       ├── paciente_service.py
│       ├── cita_service.py
│       └── resultado_service.py
├── tests/                   # Tests con pytest
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_pacientes.py
│   ├── test_citas.py
│   └── test_resultados.py
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore
├── Dockerfile               # Dockerfile para contenerización
├── docker-compose.yml       # Orquestación de contenedores
├── requirements.txt         # Dependencias de Python
├── pytest.ini              # Configuración de pytest
├── README.md               # Este archivo
└── STEPS.md                # Guía paso a paso de setup
```

## 🔐 Seguridad

- Nunca commits el archivo `.env` con credenciales reales
- Usa variables de entorno para información sensible
- En producción, usa HTTPS
- Implementa autenticación y autorización según necesites
- Mantén las dependencias actualizadas

## 🚀 Despliegue

Ver [STEPS.md](STEPS.md) para instrucciones detalladas de despliegue.

### Opciones de Despliegue
- **Heroku**: Con Dockerfile incluido
- **Railway**: Soporte nativo para FastAPI
- **Vercel**: Con adaptador para FastAPI
- **AWS/GCP/Azure**: Con Docker o servicios nativos
- **DigitalOcean**: App Platform o Droplets

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Autores

- VitalApp Team

## 🙏 Agradecimientos

- FastAPI por el excelente framework
- Supabase por la infraestructura de base de datos
- La comunidad de Python

---

Para más detalles sobre la configuración y despliegue, consulta [STEPS.md](STEPS.md)