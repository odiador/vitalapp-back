from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class ResultadoBase(BaseModel):
    """Base schema for Resultado"""
    paciente_id: int
    tipo_examen: str
    fecha_examen: datetime
    resultado: str
    observaciones: Optional[str] = None


class ResultadoCreate(ResultadoBase):
    """Schema for creating a Resultado"""
    pass


class ResultadoUpdate(BaseModel):
    """Schema for updating a Resultado"""
    tipo_examen: Optional[str] = None
    fecha_examen: Optional[datetime] = None
    resultado: Optional[str] = None
    observaciones: Optional[str] = None


class ResultadoResponse(ResultadoBase):
    """Schema for Resultado response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
