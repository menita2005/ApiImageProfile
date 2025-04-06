from sqlalchemy.orm import Session
from models import Usuario
from typing import List

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear_usuario(self, usuario_data: dict):
        db_usuario = Usuario(**usuario_data)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    

    def obtener_por_id(self, usuario_id: int):
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    def obtener_todos(self) -> List[Usuario]:
        return self.db.query(Usuario).all()