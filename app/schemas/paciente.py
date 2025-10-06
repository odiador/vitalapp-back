from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


class PacienteBase(BaseModel):
    """Base schema for Paciente"""
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    direccion: Optional[str] = None


class PacienteCreate(PacienteBase):
    """Schema for creating a Paciente"""
    pass


class PacienteUpdate(BaseModel):
    """Schema for updating a Paciente"""
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    direccion: Optional[str] = None


class PacienteResponse(PacienteBase):
    """Schema for Paciente response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
