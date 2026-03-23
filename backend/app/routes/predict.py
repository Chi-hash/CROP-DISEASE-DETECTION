from fastapi import APIRouter, File, UploadFile, HTTPException
from datetime import datetime, timezone
from app.models.schemas import PredictionResult
from app.services import ai_service, disease_service

router = APIRouter(prefix="/predict", tags=["predict"])

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


@router.post("", response_model=PredictionResult)
async def predict_disease(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported image format '{file.content_type}'. Use JPEG, PNG, or WEBP.",
        )

    image_bytes = await file.read()

    if len(image_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Image file too large. Maximum size is 5MB.",
        )

    if len(image_bytes) < 1000:
        raise HTTPException(
            status_code=400,
            detail="Image is too small or corrupted. Please upload a clear leaf photograph.",
        )

    predictions = await ai_service.predict(image_bytes)

    if not predictions:
        raise HTTPException(
            status_code=422,
            detail="Could not analyse the image. Please ensure the photo shows a plant leaf clearly.",
        )

    top = predictions[0]
    alternatives = predictions[1:]
    disease_detail = disease_service.get_disease_by_id(top.disease_id)

    return PredictionResult(
        status="success",
        top_prediction=top,
        alternatives=alternatives,
        disease_detail=disease_detail,
        analyzed_at=datetime.now(timezone.utc).isoformat(),
    )
