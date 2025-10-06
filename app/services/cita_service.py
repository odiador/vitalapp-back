from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.cita import Cita
from app.schemas.cita import CitaCreate, CitaUpdate


class CitaService:
    """Service for Cita CRUD operations"""
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Cita]:
        """Get all citas"""
        return db.query(Cita).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_id(db: Session, cita_id: int) -> Optional[Cita]:
        """Get a cita by ID"""
        return db.query(Cita).filter(Cita.id == cita_id).first()
    
    @staticmethod
    def get_by_paciente(db: Session, paciente_id: int) -> List[Cita]:
        """Get all citas for a paciente"""
        return db.query(Cita).filter(Cita.paciente_id == paciente_id).all()
    
    @staticmethod
    def create(db: Session, cita: CitaCreate) -> Cita:
        """Create a new cita"""
        db_cita = Cita(**cita.model_dump())
        db.add(db_cita)
        db.commit()
        db.refresh(db_cita)
        return db_cita
    
    @staticmethod
    def update(db: Session, cita_id: int, cita: CitaUpdate) -> Optional[Cita]:
        """Update a cita"""
        db_cita = CitaService.get_by_id(db, cita_id)
        if not db_cita:
            return None
        
        update_data = cita.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_cita, field, value)
        
        db.commit()
        db.refresh(db_cita)
        return db_cita
    
    @staticmethod
    def delete(db: Session, cita_id: int) -> bool:
        """Delete a cita"""
        db_cita = CitaService.get_by_id(db, cita_id)
        if not db_cita:
            return False
        
        db.delete(db_cita)
        db.commit()
        return True
