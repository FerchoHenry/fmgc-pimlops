# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 - HENRY DATA SCIENCE** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

¡Primer proyecto individual de la etapa de labs! En esta ocasión, se realizó un trabajo situándonos en el rol de un ***MLOps Engineer***.  
![RS](https://user-images.githubusercontent.com/50820635/85274861-7e0e3b00-b4ba-11ea-8cd3-2690ec55a67a.jpg)


### Table of Contents

1. [Descripción](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#descripci%C3%B3n)
2. [Estructura del proyecto](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#estructura-del-proyecto)
3. [Consigna](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#consigna-del-proyecto)
4. [Requerimientos](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#requerimientos-del-proyecto-requerimientos-de-aprobaci%C3%B3n)
5. [Deploy](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#Deploy)
6. [Recomendador](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#requerimientos-del-proyecto-requerimientos-de-aprobaci%C3%B3n)
7. [Material de Apoyo](https://github.com/FerchoHenry/fmgc-pimlops?tab=readme-ov-file#material-de-apoyo)

## **Descripción:**

Este proyecto forma parte del Primer Proyecto de Data Science del curso de Henry. El objetivo principal es desarrollar un    **`MVP`** (_Minimum Viable Product_) de un recomendador de películas, se adopto para el mismo el algoritmo de similitud de coseno basado en el análisis de las reseñas de las películas mediante la técnica de TF-IDF.

El proyecto se enfoca en utilizar el procesamiento del lenguaje natural (NLP) para transformar las reseñas en representaciones numéricas que permitan comparar películas entre sí y generar recomendaciones.

El ciclo de vida de este proyecto de Machine Learning contempla desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML.

## Estructura del proyecto:
El proyecto está estructurado de la siguiente manera:

<p align="center">
<img src="https://github.com/FerchoHenry/fmgc-pimlops/blob/main/imagenes/estructuraproyecto.png"  height=500>
</p>

## Consigna del proyecto

En nuestro roll como  **`Data Scientist`** se nos solicita desarrollar un **`MVP`** (_Minimum Viable Product_)  de un sistema de recomendación para poner en marcha! 

Se nos proporciona unos dataset con contenido detallado de peliculas y otro con la informacion acerca del casting y directores que participaron en ellas.
Se pueden acceder a los mismos en el siguiente enlace:
+ [Dataset](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5?usp=drive_link): Carpeta con los 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv), tener en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
#### Nota:  
No se alojan en este repositorio debido a su peso.

## **Requerimientos del proyecto (requerimientos de aprobación)**

**`Transformaciones`**: 

+ Algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder  y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** deben eliminarse.

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.

+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
  
+ def **cantidad_filmaciones_mes( *`Mes`* )**:
    Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en el mes de `X`*
         

+ def **cantidad_filmaciones_dia( *`Dia`* )**:
    Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en los días `X`*

+ def **score_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La película `X` fue estrenada en el año `X` con un score/popularidad de `X`*

+ def **votos_titulo( *`titulo_de_la_filmación`* )**:
    Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La película `X` fue estrenada en el año `X`. La misma cuenta con un total de `X` valoraciones, con un promedio de `X`*

+ def **get_actor( *`nombre_actor`* )**:
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. **La definición no deberá considerar directores.**
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *El actor `X` ha participado de `X` cantidad de filmaciones, el mismo ha conseguido un retorno de `X` con un promedio de `X` por filmación*

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.



<br/>


## `Implementación (Deployment)`**:  
La API se despliega en la nube utilizando la plataforma Render. Render permite alojar y servir la API para que los usuarios puedan acceder a ella desde un navegador web.

Debera realizarse via [Render](https://render.com/docs/free#free-web-services) y se puede consultar un [tutorial de Render](https://github.com/HX-FNegrete/render-fastapi-tutorial).   
Tambien se puede usar [Railway](https://railway.app/), o cualquier otro servicio que permita que la API pueda ser consumida desde la web.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Una vez realizado el ETL se debera generar un reporte EDA investigando las relaciones que hay entre las variables de los datasets, viendo si hay outliers o anomalías y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. 

## **`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. El EDA debería incluir gráficas interesantes para extraer datos, como por ejemplo una nube de palabras con las palabras más frecuentes en los títulos de las películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:


+ def **recomendacion( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

<br/>

**`Video`**: Sea añade un viedo a fin de mostrar que las herramientas funcionan realmente! mostrando el resultado de las consultas propuestas del modelo de ML entrenado!

## **Material de apoyo**

En este repositorio se puede encontrar algunos [links de ayuda](hhttps://github.com/HX-PRomero/PI_ML_OPS/raw/main/Material%20de%20apoyo.md). 



  
<br/>
