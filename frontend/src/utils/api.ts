import axios from 'axios'
import type { Disease, PredictionResult } from '../types'

const BASE_URL = '/api'

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
