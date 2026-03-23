import type { DiagnosisRecord } from '../types'

const STORAGE_KEY = 'cropcare_history'
const MAX_RECORDS = 10

export function getHistory(): DiagnosisRecord[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch {
    return []
  }
}

export function saveToHistory(record: DiagnosisRecord): void {
  const history = getHistory()
  const updated = [record, ...history].slice(0, MAX_RECORDS)
  localStorage.setItem(STORAGE_KEY, JSON.stringify(updated))
}

export function clearHistory(): void {
  localStorage.removeItem(STORAGE_KEY)
}
