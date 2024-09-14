#extraido de https://fastapi.tiangolo.com/tutorial/first-steps/
import pandas as pd
from fastapi import FastAPI
#from typing import Optional

# Cargar el dataset
df = pd.read_parquet('../data/movies_etl.parquet')


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola Carola3"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# ejemplo: http://127.0.0.1:8000/items/42?q=example
# respuesta: {"item_id":42,"q":"example"}

#1_ Cantidad de filmaciones mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    # Convertir el nombre del mes a minúsculas
    mes = mes.lower()
    
    # Mapeo de meses en español a números
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
        
    mes_numero = meses[mes]
    
    # Filtrar por mes de estreno
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    filmaciones_mes = df[df['release_date'].dt.month == mes_numero]
    
    return {
        "mensaje": f"{len(filmaciones_mes)} películas fueron estrenadas en el mes de {mes.capitalize()}."
    }