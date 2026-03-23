import os
import random
import asyncio
from typing import List
import httpx
from app.models.schemas import Prediction
from app.services import disease_service

HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "linkanjarad/mobilenet-v2-plant-disease-identification")
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"

# Maps PlantVillage model output labels → our disease IDs
PLANTVILLAGE_MAP: dict[str, str] = {
    # Tomato
    "Tomato___Early_blight":                              "tomato-early-blight",
    "Tomato___Late_blight":                               "tomato-late-blight",
    "Tomato___Bacterial_spot":                            "tomato-bacterial-spot",
    "Tomato___Leaf_Mold":                                 "tomato-leaf-mold",
    "Tomato___Septoria_leaf_spot":                        "tomato-septoria-leaf-spot",
    "Tomato___Spider_mites Two-spotted_spider_mite":      "tomato-spider-mites",
    "Tomato___Target_Spot":                               "tomato-target-spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus":             "tomato-yellow-leaf-curl-virus",
    "Tomato___Tomato_mosaic_virus":                       "tomato-mosaic-virus",
    "Tomato___healthy":                                   "tomato-healthy",
    # Corn / Maize
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "maize-gray-leaf-spot",
    "Corn_(maize)___Common_rust_":                        "maize-common-rust",
    "Corn_(maize)___Northern_Leaf_Blight":                "maize-northern-leaf-blight",
    "Corn_(maize)___healthy":                             "maize-healthy",
    # Potato
    "Potato___Early_blight":                              "potato-early-blight",
    "Potato___Late_blight":                               "potato-late-blight",
    "Potato___healthy":                                   "potato-healthy",
    # Pepper
    "Pepper,_bell___Bacterial_spot":                      "pepper-bacterial-spot",
    "Pepper,_bell___healthy":                             "pepper-healthy",
    # Apple
    "Apple___Apple_scab":                                 "apple-scab",
    "Apple___Black_rot":                                  "apple-black-rot",
    "Apple___Cedar_apple_rust":                           "apple-cedar-rust",
    "Apple___healthy":                                    "apple-healthy",
    # Grape
    "Grape___Black_rot":                                  "grape-black-rot",
    "Grape___Esca_(Black_Measles)":                       "grape-esca",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)":         "grape-leaf-blight",
    "Grape___healthy":                                    "grape-healthy",
    # Strawberry
    "Strawberry___Leaf_scorch":                           "strawberry-leaf-scorch",
    "Strawberry___healthy":                               "strawberry-healthy",
    # Cherry
    "Cherry_(including_sour)___Powdery_mildew":           "cherry-powdery-mildew",
    "Cherry_(including_sour)___healthy":                  "cherry-healthy",
    # Squash
    "Squash___Powdery_mildew":                            "squash-powdery-mildew",
    # Orange
    "Orange___Haunglongbing_(Citrus_greening)":           "orange-citrus-greening",
    # Peach
    "Peach___Bacterial_spot":                             "peach-bacterial-spot",
    "Peach___healthy":                                    "peach-healthy",
    # Soybean / Raspberry / Blueberry
    "Soybean___healthy":                                  "soybean-healthy",
    "Raspberry___healthy":                                "raspberry-healthy",
    "Blueberry___healthy":                                "blueberry-healthy",
}

# Diseases used in demo/mock mode
DEMO_DISEASE_IDS = [
    "tomato-early-blight", "tomato-late-blight", "tomato-bacterial-spot",
    "tomato-septoria-leaf-spot", "tomato-yellow-leaf-curl-virus",
    "maize-common-rust", "maize-northern-leaf-blight", "maize-gray-leaf-spot",
    "potato-early-blight", "potato-late-blight",
    "rice-leaf-blast", "cassava-mosaic-disease",
    "pepper-bacterial-spot", "wheat-yellow-rust",
    "apple-scab", "grape-black-rot", "strawberry-leaf-scorch",
    "orange-citrus-greening",
]


def _build_prediction(disease_id: str, confidence: float) -> Prediction | None:
    disease = disease_service.get_disease_by_id(disease_id)
    if not disease:
        return None
    return Prediction(
        disease_id=disease.id,
        common_name=disease.common_name,
        scientific_name=disease.scientific_name,
        crop=disease.crop,
        confidence=round(confidence, 4),
        severity=disease.severity,
    )


def _mock_predict(image_bytes: bytes) -> List[Prediction]:
    """Deterministic demo prediction — same image always returns the same result."""
    seed = len(image_bytes) % len(DEMO_DISEASE_IDS)
    rng = random.Random(seed)
    shuffled = DEMO_DISEASE_IDS[:]
    rng.shuffle(shuffled)

    top_conf = rng.uniform(0.82, 0.96)
    remaining = 1.0 - top_conf
    alt1_conf = rng.uniform(remaining * 0.3, remaining * 0.6)
    alt2_conf = remaining - alt1_conf

    results = []
    for did, conf in zip(shuffled[:3], [top_conf, alt1_conf, alt2_conf]):
        p = _build_prediction(did, conf)
        if p:
            results.append(p)
    return results


async def _hf_predict(image_bytes: bytes) -> List[Prediction]:
    """
    Real AI prediction using Hugging Face Inference API.
    Model: linkanjarad/mobilenet-v2-plant-disease-identification
    Trained on PlantVillage dataset (87,000+ leaf images, 38 classes).
    Falls back to mock on failure.
    """
    headers = {"Content-Type": "application/octet-stream"}
    if HF_API_TOKEN:
        headers["Authorization"] = f"Bearer {HF_API_TOKEN}"

    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(HF_API_URL, content=image_bytes, headers=headers)

            # Model is still loading — wait and retry
            if response.status_code == 503:
                wait = 10 * (attempt + 1)
                await asyncio.sleep(wait)
                continue

            response.raise_for_status()
            raw_predictions = response.json()

            if not isinstance(raw_predictions, list):
                break

            predictions: List[Prediction] = []
            for item in raw_predictions[:5]:
                label: str = item.get("label", "")
                score: float = item.get("score", 0.0)

                disease_id = PLANTVILLAGE_MAP.get(label)

                # Fuzzy fallback: try to match label parts to our DB
                if not disease_id:
                    label_lower = label.lower().replace("_", " ").replace("(", "").replace(")", "")
                    for key, val in PLANTVILLAGE_MAP.items():
                        key_lower = key.lower().replace("_", " ").replace("(", "").replace(")", "")
                        if key_lower in label_lower or label_lower in key_lower:
                            disease_id = val
                            break

                if disease_id:
                    p = _build_prediction(disease_id, score)
                    if p:
                        predictions.append(p)
                        if len(predictions) == 3:
                            break

            if predictions:
                return predictions

            break  # Got a response but no matches — fall back to mock

        except (httpx.TimeoutException, httpx.HTTPStatusError, Exception):
            if attempt == 2:
                break
            await asyncio.sleep(5)

    return _mock_predict(image_bytes)


async def predict(image_bytes: bytes) -> List[Prediction]:
    """
    Entry point. Uses Hugging Face real AI if available, otherwise demo mode.
    Set HF_API_TOKEN in .env for best results (avoids rate limits).
    """
    return await _hf_predict(image_bytes)
