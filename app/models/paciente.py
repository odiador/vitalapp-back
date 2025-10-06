from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Paciente(Base):
    """Modelo de paciente"""
    __tablename__ = "pacientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    direccion = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    citas = relationship("Cita", back_populates="paciente", cascade="all, delete-orphan")
    resultados = relationship("Resultado", back_populates="paciente", cascade="all, delete-orphan")
