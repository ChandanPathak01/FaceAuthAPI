from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routers import register, match

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Face Matching API", description= "Register users and match faces by Aadhaar", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

app.include_router(register.router)
app.include_router(match.router)

@app.get("/")
def read_root():
    return {"message": "Face Matching API is running"}