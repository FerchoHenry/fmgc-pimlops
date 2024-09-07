#extraido de https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola Carola"}