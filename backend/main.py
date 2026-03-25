"""
Vercel FastAPI entrypoint: the platform looks for `app` in `main.py` at the
project root (not under `api/`). Re-exports the real application from `app.main`.
"""
from app.main import app

__all__ = ["app"]
