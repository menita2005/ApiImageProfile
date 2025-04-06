from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session  # Importación añadida
from database import get_db
from usuario_repository import UsuarioRepository
from schemas import UsuarioCreate, UsuarioResponse
from datetime import date
from typing import List
from models import Usuario

app = FastAPI(title="API de Usuarios", version="1.0.0")

@app.get("/usuarios/", response_model=List[UsuarioResponse])
def get_usuarios(db: Session = Depends(get_db)):
    """
    Obtiene todos los usuarios registrados en la base de datos.
    
    Returns:
        List[UsuarioResponse]: Lista de usuarios con sus datos básicos
    """
    try:
        usuarios = db.query(Usuario).all()
        return usuarios
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener usuarios: {str(e)}"
        )

# Crear usuario
@app.post("/usuarios/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    try:
        return repo.crear_usuario(usuario.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Obtener usuario por ID
@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    usuario = repo.obtener_por_id(usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con ID {usuario_id} no encontrado"
        )
    return usuario