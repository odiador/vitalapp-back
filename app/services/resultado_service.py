from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.resultado import Resultado
from app.schemas.resultado import ResultadoCreate, ResultadoUpdate


class ResultadoService:
    """Service for Resultado CRUD operations"""
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Resultado]:
        """Get all resultados"""
        return db.query(Resultado).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_id(db: Session, resultado_id: int) -> Optional[Resultado]:
        """Get a resultado by ID"""
        return db.query(Resultado).filter(Resultado.id == resultado_id).first()
    
    @staticmethod
    def get_by_paciente(db: Session, paciente_id: int) -> List[Resultado]:
        """Get all resultados for a paciente"""
        return db.query(Resultado).filter(Resultado.paciente_id == paciente_id).all()
    
    @staticmethod
    def create(db: Session, resultado: ResultadoCreate) -> Resultado:
        """Create a new resultado"""
        db_resultado = Resultado(**resultado.model_dump())
        db.add(db_resultado)
        db.commit()
        db.refresh(db_resultado)
        return db_resultado
    
    @staticmethod
    def update(db: Session, resultado_id: int, resultado: ResultadoUpdate) -> Optional[Resultado]:
        """Update a resultado"""
        db_resultado = ResultadoService.get_by_id(db, resultado_id)
        if not db_resultado:
            return None
        
        update_data = resultado.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_resultado, field, value)
        
        db.commit()
        db.refresh(db_resultado)
        return db_resultado
    
    @staticmethod
    def delete(db: Session, resultado_id: int) -> bool:
        """Delete a resultado"""
        db_resultado = ResultadoService.get_by_id(db, resultado_id)
        if not db_resultado:
            return False
        
        db.delete(db_resultado)
        db.commit()
        return True
