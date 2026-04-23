from dotenv import load_dotenv
load_dotenv()

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_tailwind import tailwind
from os import path
from app.core.logging import config_logger
from app.api.v1 import v1_router
from app.api.view_router import router as view_router
from app.db.session import create_pg

input_css = path.join('app', 'public', 'css', 'input.css')
output_css = path.join('app', 'public', 'css', 'output.css')

@asynccontextmanager
async def lifespan(_: FastAPI):
    config_logger()
    create_pg()
    process = tailwind.compile(output_css, tailwind_stylesheet_path=input_css)
    yield
    process.terminate()

app = FastAPI(lifespan=lifespan)
app.mount('/public', StaticFiles(directory='app/public'), name='public')
app.include_router(view_router)
app.include_router(v1_router)
