from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.cita import CitaCreate, CitaUpdate, CitaResponse
from app.services.cita_service import CitaService
from app.services.paciente_service import PacienteService

router = APIRouter(prefix="/citas", tags=["citas"])


@router.get("/", response_model=List[CitaResponse])
def get_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all citas"""
    citas = CitaService.get_all(db, skip=skip, limit=limit)
    return citas


@router.get("/{cita_id}", response_model=CitaResponse)
def get_cita(cita_id: int, db: Session = Depends(get_db)):
    """Get a cita by ID"""
    cita = CitaService.get_by_id(db, cita_id)
    if not cita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita not found"
        )
    return cita


@router.get("/paciente/{paciente_id}", response_model=List[CitaResponse])
def get_citas_by_paciente(paciente_id: int, db: Session = Depends(get_db)):
    """Get all citas for a paciente"""
    # Verify paciente exists
    paciente = PacienteService.get_by_id(db, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return CitaService.get_by_paciente(db, paciente_id)


@router.post("/", response_model=CitaResponse, status_code=status.HTTP_201_CREATED)
def create_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    """Create a new cita"""
    # Verify paciente exists
    paciente = PacienteService.get_by_id(db, cita.paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return CitaService.create(db, cita)


@router.put("/{cita_id}", response_model=CitaResponse)
def update_cita(cita_id: int, cita: CitaUpdate, db: Session = Depends(get_db)):
    """Update a cita"""
    updated_cita = CitaService.update(db, cita_id, cita)
    if not updated_cita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita not found"
        )
    return updated_cita


@router.delete("/{cita_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cita(cita_id: int, db: Session = Depends(get_db)):
    """Delete a cita"""
    deleted = CitaService.delete(db, cita_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita not found"
        )
    return None
