from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteUpdate


class PacienteService:
    """Service for Paciente CRUD operations"""
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Paciente]:
        """Get all pacientes"""
        return db.query(Paciente).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_id(db: Session, paciente_id: int) -> Optional[Paciente]:
        """Get a paciente by ID"""
        return db.query(Paciente).filter(Paciente.id == paciente_id).first()
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[Paciente]:
        """Get a paciente by email"""
        return db.query(Paciente).filter(Paciente.email == email).first()
    
    @staticmethod
    def create(db: Session, paciente: PacienteCreate) -> Paciente:
        """Create a new paciente"""
        db_paciente = Paciente(**paciente.model_dump())
        db.add(db_paciente)
        db.commit()
        db.refresh(db_paciente)
        return db_paciente
    
    @staticmethod
    def update(db: Session, paciente_id: int, paciente: PacienteUpdate) -> Optional[Paciente]:
        """Update a paciente"""
        db_paciente = PacienteService.get_by_id(db, paciente_id)
        if not db_paciente:
            return None
        
        update_data = paciente.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_paciente, field, value)
        
        db.commit()
        db.refresh(db_paciente)
        return db_paciente
    
    @staticmethod
    def delete(db: Session, paciente_id: int) -> bool:
        """Delete a paciente"""
        db_paciente = PacienteService.get_by_id(db, paciente_id)
        if not db_paciente:
            return False
        
        db.delete(db_paciente)
        db.commit()
        return True
