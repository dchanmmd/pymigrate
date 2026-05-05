from dotenv import load_dotenv
load_dotenv()

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import path
from app.core.logging import config_logger
from app.api.v1 import v1_router
from app.db.session import create_postgres

input_css = path.join('app', 'public', 'css', 'input.css')
output_css = path.join('app', 'public', 'css', 'output.css')

@asynccontextmanager
async def lifespan(_: FastAPI):
    config_logger()
    create_postgres()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1_router)
