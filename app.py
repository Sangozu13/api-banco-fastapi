from fastapi import FastAPI
from routes.banco import banco

app = FastAPI()

app.include_router(banco)