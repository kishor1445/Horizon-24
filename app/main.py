from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .routers import events, admin

app = FastAPI(debug=True)

app.add_middleware(CORSMiddleware, allow_origins=["*"])

for api in (events, admin):
    app.include_router(api.router)

app.mount("/static", StaticFiles(directory="static"), name="Static")
