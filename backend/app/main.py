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

# Disease library images: `public/static` (Vercel CDN + local uvicorn) or legacy `static/`.
_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_public_static = os.path.join(_base, "public", "static")
_legacy_static = os.path.join(_base, "static")
static_dir = _public_static if os.path.isdir(_public_static) else _legacy_static
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=os.path.abspath(static_dir)), name="static")


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
