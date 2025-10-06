from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.paciente import PacienteCreate, PacienteUpdate, PacienteResponse
from app.services.paciente_service import PacienteService

router = APIRouter(prefix="/pacientes", tags=["pacientes"])


@router.get("/", response_model=List[PacienteResponse])
def get_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all pacientes"""
    pacientes = PacienteService.get_all(db, skip=skip, limit=limit)
    return pacientes


@router.get("/{paciente_id}", response_model=PacienteResponse)
def get_paciente(paciente_id: int, db: Session = Depends(get_db)):
    """Get a paciente by ID"""
    paciente = PacienteService.get_by_id(db, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return paciente


@router.post("/", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED)
def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    """Create a new paciente"""
    # Check if email already exists
    existing_paciente = PacienteService.get_by_email(db, paciente.email)
    if existing_paciente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return PacienteService.create(db, paciente)


@router.put("/{paciente_id}", response_model=PacienteResponse)
def update_paciente(
    paciente_id: int,
    paciente: PacienteUpdate,
    db: Session = Depends(get_db)
):
    """Update a paciente"""
    updated_paciente = PacienteService.update(db, paciente_id, paciente)
    if not updated_paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return updated_paciente


@router.delete("/{paciente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    """Delete a paciente"""
    deleted = PacienteService.delete(db, paciente_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return None
