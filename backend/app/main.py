import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from app.routes import predict, diseases
from app.services import disease_service
from app.models.schemas import HealthResponse

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    disease_service.load_diseases()
    yield


app = FastAPI(
    title="AgriScan API",
    description="AI-powered crop disease detection for smallholder farmers",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)
app.include_router(diseases.router)

# Serve downloaded disease images as static files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health_check():
    return HealthResponse(
        status="healthy",
        model_version="1.0.0-demo",
        disease_count=disease_service.get_disease_count(),
        message="AgriScan is running. Upload a leaf image to /predict to get started.",
    )


@app.get("/", tags=["system"])
def root():
    return {
        "name": "AgriScan API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }
