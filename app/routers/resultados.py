from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.resultado import ResultadoCreate, ResultadoUpdate, ResultadoResponse
from app.services.resultado_service import ResultadoService
from app.services.paciente_service import PacienteService

router = APIRouter(prefix="/resultados", tags=["resultados"])


@router.get("/", response_model=List[ResultadoResponse])
def get_resultados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all resultados"""
    resultados = ResultadoService.get_all(db, skip=skip, limit=limit)
    return resultados


@router.get("/{resultado_id}", response_model=ResultadoResponse)
def get_resultado(resultado_id: int, db: Session = Depends(get_db)):
    """Get a resultado by ID"""
    resultado = ResultadoService.get_by_id(db, resultado_id)
    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resultado not found"
        )
    return resultado


@router.get("/paciente/{paciente_id}", response_model=List[ResultadoResponse])
def get_resultados_by_paciente(paciente_id: int, db: Session = Depends(get_db)):
    """Get all resultados for a paciente"""
    # Verify paciente exists
    paciente = PacienteService.get_by_id(db, paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return ResultadoService.get_by_paciente(db, paciente_id)


@router.post("/", response_model=ResultadoResponse, status_code=status.HTTP_201_CREATED)
def create_resultado(resultado: ResultadoCreate, db: Session = Depends(get_db)):
    """Create a new resultado"""
    # Verify paciente exists
    paciente = PacienteService.get_by_id(db, resultado.paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente not found"
        )
    return ResultadoService.create(db, resultado)


@router.put("/{resultado_id}", response_model=ResultadoResponse)
def update_resultado(
    resultado_id: int,
    resultado: ResultadoUpdate,
    db: Session = Depends(get_db)
):
    """Update a resultado"""
    updated_resultado = ResultadoService.update(db, resultado_id, resultado)
    if not updated_resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resultado not found"
        )
    return updated_resultado


@router.delete("/{resultado_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resultado(resultado_id: int, db: Session = Depends(get_db)):
    """Delete a resultado"""
    deleted = ResultadoService.delete(db, resultado_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resultado not found"
        )
    return None
