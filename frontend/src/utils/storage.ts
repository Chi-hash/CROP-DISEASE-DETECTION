import type { DiagnosisRecord } from '../types'

const STORAGE_KEY = 'agriscan_history'
const MAX_RECORDS = 10

export function getHistory(): DiagnosisRecord[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) return []
    const records: DiagnosisRecord[] = JSON.parse(raw)
    // Strip any records whose preview is a dead blob URL (can't survive page refresh)
    return records.map(r => ({
      ...r,
      image_preview: r.image_preview?.startsWith('blob:') ? '' : r.image_preview,
    }))
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
