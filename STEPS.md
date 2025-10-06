# VitalApp Backend - Guía de Setup y Despliegue

Esta guía proporciona instrucciones paso a paso para configurar, desarrollar y desplegar VitalApp Backend.

## 📋 Tabla de Contenidos

1. [Setup Inicial](#setup-inicial)
2. [Configuración de Supabase](#configuración-de-supabase)
3. [Configuración Local](#configuración-local)
4. [Ejecutar la Aplicación](#ejecutar-la-aplicación)
5. [Pruebas](#pruebas)
6. [Docker](#docker)
7. [Despliegue](#despliegue)

## 🎯 Setup Inicial

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/odiador/vitalapp-back.git
cd vitalapp-back
```

### Paso 2: Crear Entorno Virtual

#### En Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🗄️ Configuración de Supabase

### Paso 1: Crear Proyecto en Supabase

1. Ve a [supabase.com](https://supabase.com)
2. Haz clic en "Start your project"
3. Inicia sesión o crea una cuenta
4. Crea un nuevo proyecto:
   - **Name**: VitalApp
   - **Database Password**: Genera una contraseña segura (guárdala)
   - **Region**: Elige la más cercana a tu ubicación
5. Espera 2-3 minutos mientras se crea el proyecto

### Paso 2: Obtener Credenciales

1. Una vez creado el proyecto, ve a **Settings** (⚙️) en el sidebar
2. Selecciona **API** en el menú de Settings
3. Copia las siguientes credenciales:
   - **Project URL** (ejemplo: `https://abcdefgh.supabase.co`)
   - **anon/public key** (empieza con `eyJ...`)
   - **service_role key** (también empieza con `eyJ...`, pero es más larga)

### Paso 3: Obtener URL de Base de Datos

1. En Settings, selecciona **Database**
2. Encuentra la sección **Connection string**
3. Selecciona el modo **URI**
4. Copia la cadena de conexión
5. Reemplaza `[YOUR-PASSWORD]` con la contraseña que generaste en el Paso 1

Formato:
```
postgresql://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
```

## ⚙️ Configuración Local

### Paso 1: Crear Archivo .env

```bash
cp .env.example .env
```

### Paso 2: Editar .env

Abre el archivo `.env` y reemplaza los valores con tus credenciales de Supabase:

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

### Paso 3: Verificar Configuración

Prueba la conexión a la base de datos:

```bash
python -c "from app.config import get_settings; s = get_settings(); print(f'URL: {s.supabase_url}')"
```

Si ves tu URL de Supabase, la configuración es correcta.

## 🚀 Ejecutar la Aplicación

### Desarrollo Local

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:
- **API**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Con Hot Reload (Recomendado para desarrollo)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Producción

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🧪 Pruebas

### Ejecutar Todos los Tests

```bash
pytest
```

### Ejecutar con Salida Detallada

```bash
pytest -v
```

### Ejecutar con Cobertura

```bash
pytest --cov=app --cov-report=html
```

Luego abre `htmlcov/index.html` en tu navegador para ver el reporte de cobertura.

### Ejecutar Tests Específicos

```bash
# Tests de salud
pytest tests/test_health.py

# Tests de pacientes
pytest tests/test_pacientes.py

# Tests de citas
pytest tests/test_citas.py

# Tests de resultados
pytest tests/test_resultados.py
```

### Ejecutar un Test Individual

```bash
pytest tests/test_pacientes.py::test_create_paciente
```

## 🐳 Docker

### Setup con Docker Compose

#### Paso 1: Configurar .env

Asegúrate de tener el archivo `.env` configurado como se indicó anteriormente.

#### Paso 2: Construir y Ejecutar

```bash
docker-compose up -d
```

Esto iniciará:
- **API**: http://localhost:8000
- **PostgreSQL**: localhost:5432

#### Paso 3: Ver Logs

```bash
docker-compose logs -f api
```

#### Paso 4: Detener

```bash
docker-compose down
```

### Usar Solo Docker (sin Compose)

#### Construir Imagen

```bash
docker build -t vitalapp-backend .
```

#### Ejecutar Contenedor

```bash
docker run -d \
  --name vitalapp-api \
  -p 8000:8000 \
  --env-file .env \
  vitalapp-backend
```

#### Ver Logs

```bash
docker logs -f vitalapp-api
```

#### Detener y Eliminar

```bash
docker stop vitalapp-api
docker rm vitalapp-api
```

## 🌐 Despliegue

### Opción 1: Heroku

#### Paso 1: Instalar Heroku CLI

```bash
# macOS
brew install heroku/brew/heroku

# Otros: https://devcenter.heroku.com/articles/heroku-cli
```

#### Paso 2: Login y Crear App

```bash
heroku login
heroku create vitalapp-backend
```

#### Paso 3: Configurar Variables de Entorno

```bash
heroku config:set SUPABASE_URL=your-supabase-url
heroku config:set SUPABASE_KEY=your-supabase-key
heroku config:set SUPABASE_SERVICE_KEY=your-service-key
heroku config:set DATABASE_URL=your-database-url
heroku config:set DEBUG=False
```

#### Paso 4: Desplegar

```bash
git push heroku main
```

#### Paso 5: Verificar

```bash
heroku open
heroku logs --tail
```

### Opción 2: Railway

#### Paso 1: Instalar Railway CLI

```bash
npm install -g @railway/cli
```

#### Paso 2: Login y Deploy

```bash
railway login
railway init
railway up
```

#### Paso 3: Configurar Variables

En el dashboard de Railway, agrega las variables de entorno del archivo `.env`.

### Opción 3: DigitalOcean App Platform

#### Paso 1: Conectar Repositorio

1. Ve a [cloud.digitalocean.com](https://cloud.digitalocean.com)
2. Crea una nueva App
3. Conecta tu repositorio de GitHub

#### Paso 2: Configurar

- **Build Command**: `pip install -r requirements.txt`
- **Run Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
- **HTTP Port**: 8080

#### Paso 3: Variables de Entorno

Agrega las variables del archivo `.env` en la sección de Environment Variables.

### Opción 4: AWS (EC2 + Docker)

#### Paso 1: Crear Instancia EC2

1. Launch una instancia Ubuntu 22.04
2. Configure Security Group (puerto 8000)
3. SSH a la instancia

#### Paso 2: Instalar Docker

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

#### Paso 3: Clonar y Configurar

```bash
git clone https://github.com/odiador/vitalapp-back.git
cd vitalapp-back
cp .env.example .env
nano .env  # Editar con tus credenciales
```

#### Paso 4: Ejecutar

```bash
docker-compose up -d
```

### Opción 5: Vercel (Serverless)

Vercel requiere un adaptador específico. Para FastAPI en Vercel:

#### Paso 1: Instalar Vercel CLI

```bash
npm install -g vercel
```

#### Paso 2: Crear vercel.json

```json
{
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

#### Paso 3: Deploy

```bash
vercel --prod
```

## 🔍 Verificación Post-Despliegue

### 1. Health Check

```bash
curl https://your-app-url.com/health
```

Respuesta esperada:
```json
{
  "status": "healthy",
  "app_name": "VitalApp Backend",
  "version": "1.0.0"
}
```

### 2. Documentación API

Visita: `https://your-app-url.com/docs`

### 3. Probar Endpoints

```bash
# Crear paciente
curl -X POST https://your-app-url.com/api/v1/pacientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan@example.com"
  }'

# Listar pacientes
curl https://your-app-url.com/api/v1/pacientes/
```

## 🐛 Troubleshooting

### Error: No se puede conectar a la base de datos

**Solución**:
1. Verifica que la URL de la base de datos sea correcta
2. Verifica que la contraseña no tenga caracteres especiales sin escapar
3. Asegúrate de que tu IP esté permitida en Supabase (por defecto, todas están permitidas)

### Error: Módulo no encontrado

**Solución**:
```bash
pip install -r requirements.txt
```

### Error: Puerto ya en uso

**Solución**:
```bash
# Linux/macOS
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Tests fallan con error de base de datos

**Solución**:
Los tests usan SQLite. Asegúrate de tener permisos de escritura en el directorio actual.

## 📚 Recursos Adicionales

- [Documentación de FastAPI](https://fastapi.tiangolo.com)
- [Documentación de Supabase](https://supabase.com/docs)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [Pytest Documentation](https://docs.pytest.org)

## 🆘 Soporte

Si encuentras problemas:
1. Revisa esta guía completa
2. Consulta los logs: `docker-compose logs -f` o `heroku logs --tail`
3. Verifica las variables de entorno
4. Abre un issue en GitHub con detalles del error

---

¡Feliz desarrollo! 🚀