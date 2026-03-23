import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import ImageUploader from '../components/ImageUploader'
import { predictDisease } from '../utils/api'
import { compressImage } from '../utils/imageUtils'
import { saveToHistory } from '../utils/storage'
import type { DiagnosisRecord } from '../types'

type Stage = 'upload' | 'preview' | 'analyzing' | 'error'

export default function Diagnose() {
  const navigate = useNavigate()
  const [stage, setStage] = useState<Stage>('upload')
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string>('')
  const [errorMsg, setErrorMsg] = useState('')

  function handleImageSelected(file: File, previewUrl: string) {
    setSelectedFile(file)
    setPreview(previewUrl)
    setStage('preview')
  }

  async function handleAnalyze() {
    if (!selectedFile) return
    setStage('analyzing')
    try {
      const compressed = await compressImage(selectedFile)
      const result = await predictDisease(compressed)

      const record: DiagnosisRecord = {
        id: crypto.randomUUID(),
        date: new Date().toISOString(),
        crop: result.top_prediction.crop,
        disease_name: result.top_prediction.common_name,
        confidence: result.top_prediction.confidence,
        severity: result.top_prediction.severity,
        image_preview: preview,
        result,
      }
      saveToHistory(record)

      navigate('/results', { state: { result, preview } })
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'Analysis failed. Please try again.'
      setErrorMsg(message.includes('Network') ? 'Cannot connect to server. Make sure the backend is running.' : message)
      setStage('error')
    }
  }

  function reset() {
    setStage('upload')
    setSelectedFile(null)
    setPreview('')
    setErrorMsg('')
  }

  return (
    <div className="min-h-screen bg-background pb-20">
      <div className="bg-primary text-white px-6 pt-10 pb-6">
        <h1 className="text-2xl font-bold">Scan Your Crop</h1>
        <p className="text-green-100 text-sm mt-1">Upload a leaf photo to get an instant disease diagnosis</p>
      </div>

      <div className="max-w-lg mx-auto px-4 py-6">
        {stage === 'upload' && (
          <ImageUploader onImageSelected={handleImageSelected} />
        )}

        {stage === 'preview' && (
          <div className="space-y-5">
            <div className="relative rounded-3xl overflow-hidden border-4 border-primary/20 shadow-lg">
              <img src={preview} alt="Selected leaf" className="w-full object-cover max-h-72" />
              <button
                onClick={reset}
                className="absolute top-3 right-3 bg-black/50 text-white rounded-full w-9 h-9 flex items-center justify-center text-lg"
              >
                ✕
              </button>
            </div>

            <div className="bg-green-50 border border-green-100 rounded-2xl p-4 text-sm text-primary">
              <p className="font-semibold mb-1">📸 Photo ready for analysis</p>
              <p className="text-green-700">Make sure the affected leaf area is clearly visible. The AI will analyse it in seconds.</p>
            </div>

            <button
              onClick={handleAnalyze}
              className="w-full bg-primary text-white font-bold text-lg py-4 rounded-2xl shadow-lg flex items-center justify-center gap-3 active:scale-95 transition-transform"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
              Analyse My Crop
            </button>

            <button onClick={reset} className="w-full text-gray-500 text-sm py-2 hover:text-gray-700">
              ← Choose a different photo
            </button>
          </div>
        )}

        {stage === 'analyzing' && (
          <div className="flex flex-col items-center justify-center py-20 gap-6">
            <div className="relative">
              <div className="w-24 h-24 rounded-full border-4 border-primary/20 border-t-primary animate-spin" />
              <span className="absolute inset-0 flex items-center justify-center text-3xl">🌿</span>
            </div>
            <div className="text-center">
              <p className="text-xl font-bold text-text-primary">Analysing your crop…</p>
              <p className="text-gray-500 text-sm mt-2">Our AI is examining the leaf for disease patterns</p>
            </div>
            {preview && (
              <img src={preview} alt="Analysing" className="w-32 h-32 rounded-2xl object-cover border-4 border-primary/30 opacity-60 animate-pulse" />
            )}
          </div>
        )}

        {stage === 'error' && (
          <div className="space-y-4 py-10 text-center">
            <div className="text-6xl">⚠️</div>
            <h2 className="text-xl font-bold text-text-primary">Analysis Failed</h2>
            <p className="text-gray-600 text-sm max-w-sm mx-auto">{errorMsg}</p>
            <button
              onClick={reset}
              className="bg-primary text-white font-semibold px-8 py-3 rounded-2xl mt-2 active:scale-95 transition-transform"
            >
              Try Again
            </button>
          </div>
        )}
      </div>
    </div>
  )
}
