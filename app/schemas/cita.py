from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class CitaBase(BaseModel):
    """Base schema for Cita"""
    paciente_id: int
    fecha_hora: datetime
    motivo: str
    estado: Optional[str] = "programada"
    notas: Optional[str] = None


class CitaCreate(CitaBase):
    """Schema for creating a Cita"""
    pass


class CitaUpdate(BaseModel):
    """Schema for updating a Cita"""
    fecha_hora: Optional[datetime] = None
    motivo: Optional[str] = None
    estado: Optional[str] = None
    notas: Optional[str] = None


class CitaResponse(CitaBase):
    """Schema for Cita response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
