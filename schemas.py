from pydantic import BaseModel, Field, HttpUrl
from datetime import date
from typing import Optional
from typing import List

# ... (otros esquemas existentes)

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50, example="Juan")
    apellido: Optional[str] = Field(None, max_length=50, example="Pérez")
    telefono: Optional[str] = Field(
        None, 
        min_length=10, 
        max_length=20, 
        pattern=r"^\+?\d{10,15}$",  # Cambiado de regex a pattern
        example="+521234567890"
    )
    fecha_nacimiento: Optional[date] = Field(
        None, 
        example="1990-01-01"
    )
    ruta_foto: Optional[HttpUrl] = Field(
        None,
        example="https://ejemplo.com/fotos/usuario.jpg"
    )

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int = Field(..., example=1)
    
    class Config:
        from_attributes = True


class UsuarioListResponse(BaseModel):
    usuarios: List[UsuarioResponse]
    
    class Config:
        from_attributes = True