#!/usr/bin/env python3
"""
Verification script to check if the VitalApp Backend is properly set up.
Run this script after installing dependencies to verify the installation.
"""

import sys
from pathlib import Path

def check_structure():
    """Check if all required files and directories exist"""
    required_paths = [
        "app/__init__.py",
        "app/main.py",
        "app/config.py",
        "app/database.py",
        "app/models/__init__.py",
        "app/models/paciente.py",
        "app/models/cita.py",
        "app/models/resultado.py",
        "app/schemas/__init__.py",
        "app/schemas/paciente.py",
        "app/schemas/cita.py",
        "app/schemas/resultado.py",
        "app/routers/__init__.py",
        "app/routers/health.py",
        "app/routers/pacientes.py",
        "app/routers/citas.py",
        "app/routers/resultados.py",
        "app/services/__init__.py",
        "app/services/paciente_service.py",
        "app/services/cita_service.py",
        "app/services/resultado_service.py",
        "tests/__init__.py",
        "tests/conftest.py",
        "tests/test_health.py",
        "tests/test_pacientes.py",
        "tests/test_citas.py",
        "tests/test_resultados.py",
        "requirements.txt",
        "Dockerfile",
        "docker-compose.yml",
        ".env.example",
        ".gitignore",
        "README.md",
        "STEPS.md",
    ]
    
    missing = []
    for path in required_paths:
        if not Path(path).exists():
            missing.append(path)
    
    if missing:
        print("❌ Missing files/directories:")
        for path in missing:
            print(f"   - {path}")
        return False
    else:
        print("✅ All required files and directories present")
        return True

def check_imports():
    """Check if all modules can be imported"""
    try:
        print("\n📦 Checking module imports...")
        
        # Check if dependencies are installed
        required_packages = [
            ("fastapi", "FastAPI"),
            ("uvicorn", "Uvicorn"),
            ("sqlalchemy", "SQLAlchemy"),
            ("pydantic", "Pydantic"),
            ("pytest", "Pytest"),
        ]
        
        missing_packages = []
        for package, name in required_packages:
            try:
                __import__(package)
                print(f"   ✓ {name} installed")
            except ImportError:
                missing_packages.append(name)
                print(f"   ✗ {name} NOT installed")
        
        if missing_packages:
            print("\n⚠️  Missing packages. Install with:")
            print("   pip install -r requirements.txt")
            return False
        
        # Try importing application modules
        print("\n🔍 Checking application modules...")
        from app import config
        print("   ✓ Config module")
        
        from app import database
        print("   ✓ Database module")
        
        from app.models import Paciente, Cita, Resultado
        print("   ✓ Models (Paciente, Cita, Resultado)")
        
        from app.schemas import PacienteCreate, CitaCreate, ResultadoCreate
        print("   ✓ Schemas (PacienteCreate, CitaCreate, ResultadoCreate)")
        
        from app.services import PacienteService, CitaService, ResultadoService
        print("   ✓ Services (PacienteService, CitaService, ResultadoService)")
        
        print("\n✅ All modules can be imported successfully")
        return True
        
    except Exception as e:
        print(f"\n❌ Import error: {e}")
        return False

def check_env_file():
    """Check if .env file exists"""
    print("\n🔧 Checking environment configuration...")
    if Path(".env").exists():
        print("   ✓ .env file found")
        return True
    else:
        print("   ⚠️  .env file not found")
        print("   ℹ️  Copy .env.example to .env and configure your Supabase credentials:")
        print("      cp .env.example .env")
        return False

def main():
    """Main verification function"""
    print("=" * 60)
    print("VitalApp Backend - Installation Verification")
    print("=" * 60)
    
    results = []
    
    # Check structure
    print("\n📁 Checking project structure...")
    results.append(check_structure())
    
    # Check imports
    results.append(check_imports())
    
    # Check .env file
    results.append(check_env_file())
    
    # Summary
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All checks passed! Your installation is ready.")
        print("\nNext steps:")
        print("1. Configure your .env file with Supabase credentials")
        print("2. Run: uvicorn app.main:app --reload")
        print("3. Visit: http://localhost:8000/docs")
        return 0
    else:
        print("⚠️  Some checks failed. Please review the output above.")
        print("\nFor help, see:")
        print("- README.md for general information")
        print("- STEPS.md for detailed setup instructions")
        return 1

if __name__ == "__main__":
    sys.exit(main())
