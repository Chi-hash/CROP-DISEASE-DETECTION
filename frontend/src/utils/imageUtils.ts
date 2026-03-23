import imageCompression from 'browser-image-compression'

const COMPRESSION_OPTIONS = {
  maxSizeMB: 0.5,
  maxWidthOrHeight: 1024,
  useWebWorker: true,
}

export async function compressImage(file: File): Promise<File> {
  if (file.size <= 500 * 1024) return file
  return imageCompression(file, COMPRESSION_OPTIONS)
}

export function fileToDataURL(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => resolve(reader.result as string)
    reader.onerror = reject
    reader.readAsDataURL(file)
  })
}

export function formatConfidence(confidence: number): string {
  return `${Math.round(confidence * 100)}%`
}

export function getSeverityColor(severity: string): string {
  switch (severity.toLowerCase()) {
    case 'severe': return 'danger'
    case 'moderate': return 'warning'
    case 'mild': return 'accent'
    case 'none': return 'accent'
    default: return 'warning'
  }
}
