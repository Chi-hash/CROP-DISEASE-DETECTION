import json
import os
from typing import List, Optional
from app.models.schemas import Disease

_diseases: List[Disease] = []


def load_diseases() -> None:
    global _diseases
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "diseases.json")
    with open(data_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    _diseases = [Disease(**d) for d in raw]


def get_all_diseases(crop: Optional[str] = None) -> List[Disease]:
    if crop:
        return [d for d in _diseases if d.crop.lower() == crop.lower()]
    return _diseases


def get_disease_by_id(disease_id: str) -> Optional[Disease]:
    for d in _diseases:
        if d.id == disease_id:
            return d
    return None


def get_disease_ids() -> List[str]:
    return [d.id for d in _diseases]


def get_crops() -> List[str]:
    return sorted(list(set(d.crop for d in _diseases)))


def get_disease_count() -> int:
    return len(_diseases)
