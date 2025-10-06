from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Resultado(Base):
    """Modelo de resultado médico"""
    __tablename__ = "resultados"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    tipo_examen = Column(String(100), nullable=False)
    fecha_examen = Column(DateTime(timezone=True), nullable=False)
    resultado = Column(Text, nullable=False)
    observaciones = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    paciente = relationship("Paciente", back_populates="resultados")
