from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Servicio de Division")

class Operacion(BaseModel):
    a: float
    b: float

@app.get("/")
def estado():
    return {"servicio": "division", "estado": "activo"}

@app.post("/division")
def dividir(datos: Operacion):
    if datos.b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
    return {"operacion": "division", "resultado": datos.a + datos.b}    