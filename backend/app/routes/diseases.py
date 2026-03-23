from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.schemas import Disease
from app.services import disease_service

router = APIRouter(prefix="/diseases", tags=["diseases"])


@router.get("", response_model=List[Disease])
def list_diseases(crop: Optional[str] = Query(default=None, description="Filter by crop name")):
    return disease_service.get_all_diseases(crop=crop)


@router.get("/crops", response_model=List[str])
def list_crops():
    return disease_service.get_crops()


@router.get("/{disease_id}", response_model=Disease)
def get_disease(disease_id: str):
    disease = disease_service.get_disease_by_id(disease_id)
    if not disease:
        raise HTTPException(status_code=404, detail=f"Disease '{disease_id}' not found")
    return disease
