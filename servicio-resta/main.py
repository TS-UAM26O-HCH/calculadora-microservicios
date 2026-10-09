from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Servicio de Resta")

class Operacion(BaseModel):
    a: float
    b: float

@app.get("/")
def estado():
    return {"servicio": "resta", "estado": "activo"}

@app.post("/resta")
def restar(datos: Operacion):
    return {"operacion": "resta", "resultado": datos.a - datos.b}