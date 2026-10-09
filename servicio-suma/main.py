from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Servicio de Suma")

class Operacion(BaseModel):
    a: float
    b: float

@app.get("/")
def estado():
    return {"servicio": "suma", "estado": "activo"}

@app.post("/suma")
def sumar(datos: Operacion):
    return {"operacion": "suma", "resultado": datos.a + datos.b}