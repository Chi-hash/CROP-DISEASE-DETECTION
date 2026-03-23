"""
Downloads real plant disease photos from iNaturalist (free, no API key needed).
Falls back to crop-specific Unsplash photos if iNaturalist has no result.

Run once from the backend folder:
    python download_disease_images.py
"""

import json
import os
import time
import httpx

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static", "images", "diseases")
DISEASES_JSON = os.path.join(os.path.dirname(__file__), "app", "data", "diseases.json")
INAT_URL = "https://api.inaturalist.org/v1/observations"

HEADERS = {
    "User-Agent": "CropCareAI/1.0 (hackathon; educational) httpx/0.27"
}

# Multiple search attempts per disease (tries each in order until one works)
INAT_QUERIES: dict[str, list[str]] = {
    "tomato-early-blight":           ["tomato early blight brown spots", "Alternaria blight tomato leaf", "tomato fungal disease leaf spots"],
    "tomato-late-blight":            ["tomato late blight disease", "Phytophthora tomato", "tomato brown rot disease"],
    "tomato-bacterial-spot":         ["tomato bacterial spot disease", "tomato leaf spot bacterial", "tomato disease spots"],
    "tomato-leaf-mold":              ["tomato leaf mold fungal", "tomato mold disease", "tomato leaf disease"],
    "tomato-septoria-leaf-spot":     ["tomato septoria leaf spot", "tomato small spots disease", "tomato leaf spots fungal"],
    "tomato-spider-mites":           ["spider mite plant damage", "Tetranychus urticae mite", "plant mite webbing damage"],
    "tomato-target-spot":            ["tomato target spot disease", "tomato brown circular spots", "Corynespora leaf spot"],
    "tomato-yellow-leaf-curl-virus": ["tomato yellow leaf curl virus", "tomato yellowing curl disease", "tomato virus disease"],
    "tomato-mosaic-virus":           ["tomato mosaic virus disease", "tomato virus mottling", "tomato mosaic disease"],
    "tomato-healthy":                ["tomato plant healthy green", "Solanum lycopersicum", "tomato plant growing"],
    "maize-common-rust":             ["corn rust pustules", "maize rust fungal disease", "Puccinia corn leaf rust"],
    "maize-northern-leaf-blight":    ["corn leaf blight disease", "maize northern leaf blight", "corn fungal blight"],
    "maize-gray-leaf-spot":          ["corn gray leaf spot", "maize gray leaf spot", "corn fungal leaf lesion"],
    "maize-healthy":                 ["corn maize healthy plant", "Zea mays field crop", "maize green healthy plant"],
    "potato-early-blight":           ["potato early blight disease", "potato leaf brown spots", "Alternaria potato disease"],
    "potato-late-blight":            ["potato late blight disease", "Phytophthora potato blight", "potato blight brown"],
    "potato-healthy":                ["potato plant healthy green", "Solanum tuberosum plant", "potato crop growing"],
    "rice-leaf-blast":               ["rice blast disease leaf", "Magnaporthe rice blast", "rice leaf disease brown"],
    "cassava-mosaic-disease":        ["cassava mosaic disease", "cassava virus disease Africa", "cassava leaf mosaic"],
    "pepper-bacterial-spot":         ["pepper bacterial spot disease", "Capsicum leaf spot disease", "pepper plant disease"],
    "pepper-healthy":                ["bell pepper plant healthy", "Capsicum annuum plant", "pepper crop growing"],
    "wheat-yellow-rust":             ["wheat yellow rust disease", "wheat stripe rust", "Puccinia wheat rust yellow"],
    "apple-scab":                    ["apple scab disease", "Venturia inaequalis apple", "apple leaf scab spots"],
    "apple-black-rot":               ["apple black rot disease", "apple rot fruit disease", "apple fungal disease"],
    "apple-cedar-rust":              ["cedar apple rust orange", "Gymnosporangium rust apple", "apple rust orange spots"],
    "apple-healthy":                 ["apple tree healthy fruit", "Malus apple orchard", "apple green healthy leaves"],
    "grape-black-rot":               ["grape black rot disease", "Guignardia grape disease", "grape mummy berries rot"],
    "grape-esca":                    ["grape esca disease", "grapevine trunk disease", "grape black measles disease"],
    "grape-leaf-blight":             ["grape leaf blight disease", "grapevine leaf brown spots", "grape leaf lesion"],
    "grape-healthy":                 ["grape vine healthy green", "Vitis vinifera vineyard", "grapevine healthy leaves"],
    "strawberry-leaf-scorch":        ["strawberry leaf scorch disease", "strawberry leaf spots purple", "strawberry disease"],
    "strawberry-healthy":            ["strawberry plant healthy green", "Fragaria strawberry plant", "strawberry growing"],
    "cherry-powdery-mildew":         ["cherry powdery mildew white", "Podosphaera mildew", "cherry leaf white coating"],
    "cherry-healthy":                ["cherry tree healthy fruit", "Prunus avium cherry blossom", "cherry orchard tree"],
    "squash-powdery-mildew":         ["squash pumpkin powdery mildew", "cucurbit mildew white", "pumpkin leaf mildew white"],
    "orange-citrus-greening":        ["citrus greening disease", "Huanglongbing orange disease", "citrus HLB yellow"],
    "peach-bacterial-spot":          ["peach bacterial spot disease", "peach leaf spot disease", "Xanthomonas peach"],
    "peach-healthy":                 ["peach tree healthy fruit", "Prunus persica peach orchard", "peach fruit tree"],
    "soybean-healthy":               ["soybean plant healthy field", "Glycine max soybean", "soybean crop growing"],
    "raspberry-healthy":             ["raspberry plant healthy berries", "Rubus idaeus raspberry", "raspberry fruit cane"],
    "blueberry-healthy":             ["blueberry plant healthy berries", "Vaccinium blueberry", "blueberry fruit bush"],
}

# Unsplash photo IDs as crop-based fallbacks (verified working IDs)
UNSPLASH_FALLBACKS: dict[str, str] = {
    "tomato":      "1471194402653-db1acd0adba9",
    "maize":       "1565043589-52a8526da9e4",
    "potato":      "1624204386084-e1bde49f39e9",
    "rice":        "1536054636059-4c1376e52f87",
    "cassava":     "1500382017468-9049fed747ef",
    "pepper":      "1518977822534-7049a61ee0c2",
    "wheat":       "1566478989037-c7b0f29c2e9a",
    "apple":       "1560806887-1e4cd0b6cbd6",
    "grape":       "1516594195851-ba80e1f15af5",
    "strawberry":  "1464965911861-746a04b4bca6",
    "cherry":      "1528821128474-27f6b5930e9b",
    "squash":      "1512621776951-a57141f2eefd",
    "orange":      "1545830303-8a21752ce31a",
    "peach":       "1529566652340-5e4a0d2e9c6b",
    "soybean":     "1500382017468-9049fed747ef",
    "raspberry":   "1601004890655-5935e003b774",
    "blueberry":   "1551800843-0d9f4e3c0b9a",
    "default":     "1416879595882-3373a0480b5b",
}


def fetch_inat_photo(queries: list[str]) -> str | None:
    """Try multiple queries on iNaturalist until a photo is found."""
    for query in queries:
        params = {
            "q": query,
            "photos": "true",
            "per_page": "5",
            "order_by": "votes",
        }
        try:
            resp = httpx.get(INAT_URL, params=params, headers=HEADERS, timeout=15)
            resp.raise_for_status()
            results = resp.json().get("results", [])
            for obs in results:
                photos = obs.get("photos", [])
                if photos:
                    url: str = photos[0].get("url", "")
                    if url and "inaturalist" in url:
                        return url.replace("/square.", "/medium.")
        except Exception:
            pass
        time.sleep(0.3)
    return None


def unsplash_url(disease_id: str) -> str:
    """Build an Unsplash fallback URL based on crop type."""
    crop = disease_id.split("-")[0]
    photo_id = UNSPLASH_FALLBACKS.get(crop, UNSPLASH_FALLBACKS["default"])
    return f"https://images.unsplash.com/photo-{photo_id}?w=640&q=80&auto=format&fit=crop"


def download_image(url: str, filepath: str) -> bool:
    """Download an image from URL to filepath."""
    try:
        resp = httpx.get(url, timeout=30, follow_redirects=True, headers=HEADERS)
        resp.raise_for_status()
        content_type = resp.headers.get("content-type", "")
        if "image" not in content_type:
            return False
        with open(filepath, "wb") as f:
            f.write(resp.content)
        size_kb = len(resp.content) // 1024
        print(f"  Saved {size_kb}KB")
        return True
    except Exception as e:
        print(f"  Download failed: {e}")
        return False


def main():
    os.makedirs(STATIC_DIR, exist_ok=True)

    with open(DISEASES_JSON, encoding="utf-8") as f:
        diseases = json.load(f)

    disease_map = {d["id"]: d for d in diseases}
    inat_count = 0
    unsplash_count = 0
    total = len(INAT_QUERIES)

    for i, (disease_id, queries) in enumerate(INAT_QUERIES.items(), 1):
        if disease_id not in disease_map:
            continue

        img_path = os.path.join(STATIC_DIR, f"{disease_id}.jpg")
        local_url = f"/static/images/diseases/{disease_id}.jpg"

        if os.path.exists(img_path):
            print(f"[{i}/{total}] CACHED  {disease_id}")
            disease_map[disease_id]["image_url"] = local_url
            inat_count += 1
            continue

        print(f"[{i}/{total}] FETCH   {disease_id}")

        # Try iNaturalist first
        photo_url = fetch_inat_photo(queries)
        source = "iNaturalist"

        # Fall back to Unsplash crop photo
        if not photo_url:
            photo_url = unsplash_url(disease_id)
            source = "Unsplash (crop fallback)"

        print(f"  Source: {source}")
        print(f"  URL:    {photo_url[:75]}...")

        success = download_image(photo_url, img_path)
        if success:
            disease_map[disease_id]["image_url"] = local_url
            if source == "iNaturalist":
                inat_count += 1
            else:
                unsplash_count += 1
        else:
            print(f"  WARN: Could not download — image will use original URL")

        time.sleep(0.8)

    with open(DISEASES_JSON, "w", encoding="utf-8") as f:
        json.dump(list(disease_map.values()), f, indent=2)

    print(f"\n{'='*55}")
    print(f"Real disease photos (iNaturalist): {inat_count}")
    print(f"Crop fallback photos (Unsplash):   {unsplash_count}")
    print(f"Images saved to: {STATIC_DIR}")
    print(f"Restart the backend to serve new images.")


if __name__ == "__main__":
    main()
