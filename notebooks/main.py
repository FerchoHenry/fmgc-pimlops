#extraido de https://fastapi.tiangolo.com/tutorial/first-steps/
import pandas as pd
import numpy as np
from fastapi import FastAPI
#from typing import Optional

# Cargar el dataset
df = pd.read_parquet('../data/movies_etl3.parquet')
dfcredits = pd.read_parquet('../data/credits_etl.parquet')

#pasamos a Str la columna ID para los merges de los punto 5 y 6
dfcredits['id'] = dfcredits['id'].astype(str)


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
    
    return { "mensaje": f"La película {film_info['title']} fue estrenada en el año {roun(film_info['release_year'])} con un score/popularidad de {film_info['popularity']}"}

#4 votos titulos

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo):
    # Filtrar el DataFrame por título, paso todo a minusculas para evitar errores.
    film = df[df['title'].str.lower() == titulo.lower()]
    
    if film.empty:
        return {"error": "Película no encontrada"}
    
    #si arroja mas de un resultado me quedo con la primera
    film_info = film.iloc[0]
    
    if film_info['vote_count'] < 2000:
        return {"mensaje": "La película no cumple con el mínimo de 2000 valoraciones."}
    
    return { "mensaje": f" La pelicula {film_info['title']} fue estrenada en el año {round(film_info['release_year'])}. La misma cuenta con un total de {round(film_info['vote_count'])} valoraciones, con un promedio de {film_info['vote_average']}"}  

#5 get actor

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor):
    # Filtrar el DataFrame por actor
    films_actor = dfcredits[dfcredits['cast'].str.contains(nombre_actor, case=False, na=False)]
    
    if films_actor.empty:
        return {"error": "Actor no encontrado"}
    
    merge_dfrev = pd.merge(df[['id','revenue']], films_actor, on='id', how='right')
    
    cantidad_filmaciones = len(films_actor)
    retorno_total = merge_dfrev['revenue'].sum()
    promedio_retorno = merge_dfrev['revenue'].mean()
     
    return { "mensaje" : f"El actor {nombre_actor} ha participado de {cantidad_filmaciones} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno_total} con un promedio de {promedio_retorno:.2F} por filmación"}

# 6 get director
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director):
    # Filtrar el DataFrame por director
    films_director = dfcredits[dfcredits['crew'].str.contains(nombre_director, case=False, na=False)]
    
    if films_director.empty:
        return {"error": "Director no encontrado"}
    
    merge_crew =  pd.merge(df[['id','title','budget','release_date','revenue','return']], films_director, on='id', how='right')
    retorno_total = np.sum(merge_crew['return'][np.isfinite(merge_crew['return'])])  
    
    return { "mensaje" : f"el director {nombre_director} tiene un retorno total de: {retorno_total:.2f}" ,
            "detalle de peliculas": f"{merge_crew}"}  
             
# Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver 
# el éxito del mismo medido a través del retorno. Además, 
# deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
#exito = retorno
#nombre,fecha de lanzamiento, retorno individual, costo y ganancia 
  