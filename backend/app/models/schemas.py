from pydantic import BaseModel
from typing import List, Optional


class Treatment(BaseModel):
    organic: List[str]
    chemical: List[str]
    prevention: List[str]


class Disease(BaseModel):
    id: str
    common_name: str
    scientific_name: str
    crop: str
    severity: str
    description: str
    symptoms: List[str]
    causes: str
    treatment: Treatment
    image_url: str
    tags: List[str]


class Prediction(BaseModel):
    disease_id: str
    common_name: str
    scientific_name: str
    crop: str
    confidence: float
    severity: str


class PredictionResult(BaseModel):
    status: str
    top_prediction: Prediction
    alternatives: List[Prediction]
    disease_detail: Optional[Disease] = None
    analyzed_at: str


class HealthResponse(BaseModel):
    status: str
    model_version: str
    disease_count: int
    message: str
