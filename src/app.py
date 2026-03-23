from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database.session import engine
from src.database.base import Base

from src.routers.auth_router import router as auth_router
from src.routers.note_router import router as note_router

@asynccontextmanager
async def lifespan(app :FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield

    await engine.dispose()


app = FastAPI(
    title="Notes app",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(note_router)

@app.get("/health")
async def health_check():
    return {"status" : "Running fine"}


