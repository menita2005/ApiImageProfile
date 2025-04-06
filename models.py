from sqlalchemy import Column, Integer, String, Date
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50))
    telefono = Column(String(20))
    fecha_nacimiento = Column(Date)  # Tipo Date para fechas
    ruta_foto = Column(String(255))  # Almacena la ruta o URL de la fotoS