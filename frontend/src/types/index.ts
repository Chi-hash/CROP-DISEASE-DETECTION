export interface Treatment {
  organic: string[]
  chemical: string[]
  prevention: string[]
}

export interface Disease {
  id: string
  common_name: string
  scientific_name: string
  crop: string
  severity: 'None' | 'Mild' | 'Moderate' | 'Severe'
  description: string
  symptoms: string[]
  causes: string
  treatment: Treatment
  image_url: string
  tags: string[]
}

export interface Prediction {
  disease_id: string
  common_name: string
  scientific_name: string
  crop: string
  confidence: number
  severity: string
}

export interface PredictionResult {
  status: string
  top_prediction: Prediction
  alternatives: Prediction[]
  disease_detail: Disease | null
  analyzed_at: string
}

export interface DiagnosisRecord {
  id: string
  date: string
  crop: string
  disease_name: string
  confidence: number
  severity: string
  image_preview: string
  result: PredictionResult
}
