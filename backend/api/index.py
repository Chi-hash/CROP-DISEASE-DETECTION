import os
import sys

# Make the 'app' package importable from the parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangum import Mangum
from app.main import app as fastapi_app

# Vercel's Python runtime needs an ASGI adapter; raw FastAPI returns 404 otherwise
app = Mangum(fastapi_app, lifespan="off")
