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

#1_ Cantidad de filmaciones mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes):
        
    # Mapeo de meses
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
        "mensaje": f"{len(filmaciones_mes)} cantidad de películas fueron estrenadas en el mes de {mes}"
    }
#2_ Cantidad de filmaciones dia
    
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia):
    
    # Mapeo de días 
    dias = {
        "lunes": 0, "martes": 1, "miércoles": 2, "jueves": 3,
        "viernes": 4, "sábado": 5, "domingo": 6
    }
         
    dia_numero = dias[dia]
    
    # Filtrar por día de estreno
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    filmaciones_dia = df[df['release_date'].dt.weekday == dia_numero]
    
    return {
        "mensaje": f"{len(filmaciones_dia)} cantidad de películas fueron estrenadas en los días {dia}"
    }
3# Score titulo

@app.get("/score_titulo/{titulo}")
def score_titulo(titulo):
    # Filtrar el DataFrame por título, paso todo a minusculas para evitar errores.
    film = df[df['title'].str.lower() == titulo.lower()]
    
    if film.empty:
        return {"error": "Película no encontrada"}
    
    #si arroja mas de un resultado me quedo con la primera   
    film_info = film.iloc[0]
    
    return { "mensaje": f"La película {film_info['title']} fue estrenada en el año {film_info['release_year']} con un score/popularidad de {film_info['popularity']}"}

#4 votos titulos

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    # Filtrar el DataFrame por título, paso todo a minusculas para evitar errores.
    film = df[df['title'].str.lower() == titulo.lower()]
    
    if film.empty:
        return {"error": "Película no encontrada"}
    
    #si arroja mas de un resultado me quedo con la primera
    film_info = film.iloc[0]
    
    #if film_info['vote_count'] < 2000:
    #    return {"mensaje": "La película no cumple con el mínimo de 2000 valoraciones."}
    
    return { "mensaje": f" La pelicula {film_info['title']} fue estrenada en el año {film_info['release_year']}. La misma cuenta con un total de agregar film_info['vote_count'] valoraciones, con un promedio de {film_info['vote_average']}"}
       