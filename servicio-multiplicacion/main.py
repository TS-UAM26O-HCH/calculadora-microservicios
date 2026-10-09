from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Servicio de Multipicacion")

class Operacion(BaseModel):
    a: float
    b: float

@app.get("/")
def estado():
    return {"servicio": "multiplicacion", "estado": "activo"}

@app.post("/multiplicacion")
def multiplicar(datos: Operacion):
    return {"operacion": "multiplicacion", "resultado": datos.a * datos.b}