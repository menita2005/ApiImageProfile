from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#http://127.0.0.1:8000

class   Libro(BaseModel):
    id: int
    nombre: str
    autor: str
    precio: float   

@app.get("/")

def index():
    return {"message": "Hello, World!"}
@app.get("/libro/{id}")
def mostrar_libro(id):
    return{"data":id}

@app.post("/libro")
def crear_libro(libro: Libro):      
    return {"data": f"libro  {libro.titulo} insertado" }

@app.put("/libro/{id}")
def actualizar_libro(id:int, libro: Libro):
    return {"data": f"libro {id} actualizado"}

@app.delete("/libro/{id}")
def eliminar_libro(id:int):
    return {"data": f"libro {id} eliminado"}    
