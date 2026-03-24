import axios from 'axios'
import type { Disease, PredictionResult } from '../types'

// In development: VITE_BACKEND_URL is unset → falls back to '/api' (Vite proxy handles it)
// In production:  VITE_BACKEND_URL = 'https://agriscan-api.onrender.com' → direct backend calls
const BASE_URL = import.meta.env.VITE_BACKEND_URL ?? '/api'

const client = axios.create({ baseURL: BASE_URL })

export async function predictDisease(imageFile: File): Promise<PredictionResult> {
  const form = new FormData()
  form.append('file', imageFile)
  const { data } = await client.post<PredictionResult>('/predict', form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return data
}

export async function fetchDiseases(crop?: string): Promise<Disease[]> {
  const params = crop ? { crop } : {}
  const { data } = await client.get<Disease[]>('/diseases', { params })
  return data
}

export async function fetchDisease(id: string): Promise<Disease> {
  const { data } = await client.get<Disease>(`/diseases/${id}`)
  return data
}

export async function fetchCrops(): Promise<string[]> {
  const { data } = await client.get<string[]>('/diseases/crops')
  return data
}

/**
 * Resolves a backend-relative path (e.g. /static/images/diseases/foo.jpg)
 * to a full URL that works in both dev (Vite proxy) and production.
 */
export function getAssetUrl(path: string): string {
  const backend = import.meta.env.VITE_BACKEND_URL ?? ''
  return backend + path
}
