import { useLocation, useNavigate } from 'react-router-dom'
import type { PredictionResult } from '../types'
import SeverityBadge from '../components/SeverityBadge'
import ConfidenceGauge from '../components/ConfidenceGauge'
import TreatmentSection from '../components/TreatmentCard'
import { formatConfidence } from '../utils/imageUtils'

interface LocationState {
  result: PredictionResult
  preview: string
}

export default function Results() {
  const navigate = useNavigate()
  const location = useLocation()
  const state = location.state as LocationState | null

  if (!state?.result) {
    return (
      <div className="min-h-screen bg-background flex flex-col items-center justify-center gap-4 pb-20 px-6">
        <span className="text-6xl">🌿</span>
        <h2 className="text-xl font-bold text-text-primary">No Diagnosis Yet</h2>
        <p className="text-gray-500 text-sm text-center">Upload a leaf photo to get your crop disease diagnosis.</p>
        <button onClick={() => navigate('/diagnose')} className="bg-primary text-white font-semibold px-8 py-3 rounded-2xl">
          Scan a Crop
        </button>
      </div>
    )
  }

  const { result, preview } = state
  const { top_prediction: top, alternatives, disease_detail } = result
  const isHealthy = top.severity.toLowerCase() === 'none'

  function handleShare() {
    const text = `🌿 AgriScan Diagnosis\n\nCrop: ${top.crop}\nDisease: ${top.common_name}\nConfidence: ${formatConfidence(top.confidence)}\nSeverity: ${top.severity}\n\nDiagnosed with AgriScan 🌱`
    if (navigator.share) {
      navigator.share({ title: 'AgriScan Diagnosis', text })
    } else {
      navigator.clipboard.writeText(text).then(() => alert('Result copied to clipboard!'))
    }
  }

  return (
    <div className="min-h-screen bg-background pb-24">
      {/* Header */}
      <div className={`px-6 pt-10 pb-6 text-white ${isHealthy ? 'bg-accent' : 'bg-primary'}`}>
        <button onClick={() => navigate(-1)} className="flex items-center gap-1 text-white/80 text-sm mb-4">
          <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Back
        </button>
        <h1 className="text-2xl font-bold">{isHealthy ? '✅ Plant is Healthy!' : 'Disease Detected'}</h1>
        <p className="text-white/80 text-sm mt-1">
          {isHealthy ? 'No disease found. Keep up your good farming practices.' : 'Review the diagnosis and treatment plan below.'}
        </p>
      </div>

      <div className="max-w-lg mx-auto px-4 py-5 space-y-4">
        {/* Main Result Card */}
        <div className="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden">
          {preview && (
            <img src={preview} alt="Uploaded leaf" className="w-full h-48 object-cover" />
          )}
          <div className="p-5">
            <div className="flex items-start justify-between gap-3">
              <div>
                <h2 className="text-2xl font-extrabold text-text-primary">{top.common_name}</h2>
                <p className="text-sm text-gray-500 italic mt-0.5">{top.scientific_name}</p>
                <p className="text-sm text-gray-600 mt-1">
                  Crop: <span className="font-semibold text-text-primary">{top.crop}</span>
                </p>
              </div>
              <SeverityBadge severity={top.severity} />
            </div>

            <div className="flex items-center justify-center mt-5 pt-5 border-t border-gray-100">
              <ConfidenceGauge confidence={top.confidence} />
            </div>
          </div>
        </div>

        {/* Disease Description */}
        {disease_detail?.description && (
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
            <h3 className="font-bold text-text-primary mb-2">About This Disease</h3>
            <p className="text-sm text-gray-700 leading-relaxed">{disease_detail.description}</p>
          </div>
        )}

        {/* Symptoms */}
        {disease_detail?.symptoms && disease_detail.symptoms.length > 0 && (
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
            <h3 className="font-bold text-text-primary mb-3">Symptoms Observed</h3>
            <ul className="space-y-2">
              {disease_detail.symptoms.map((s, i) => (
                <li key={i} className="flex gap-2 text-sm text-gray-700">
                  <span className="text-warning flex-shrink-0">⚠️</span>
                  <span>{s}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Treatment */}
        {disease_detail?.treatment && (
          <div>
            <h3 className="font-bold text-text-primary mb-3 text-base">Treatment & Prevention</h3>
            <TreatmentSection
              organic={disease_detail.treatment.organic}
              chemical={disease_detail.treatment.chemical}
              prevention={disease_detail.treatment.prevention}
            />
          </div>
        )}

        {/* Alternative Predictions */}
        {alternatives.length > 0 && (
          <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
            <h3 className="font-bold text-text-primary mb-3">Other Possibilities</h3>
            <div className="space-y-2">
              {alternatives.map((alt) => (
                <div key={alt.disease_id} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                  <div>
                    <p className="text-sm font-medium text-text-primary">{alt.common_name}</p>
                    <p className="text-xs text-gray-500">{alt.crop}</p>
                  </div>
                  <div className="flex items-center gap-2">
                    <div className="w-20 h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-primary/40 rounded-full"
                        style={{ width: `${Math.round(alt.confidence * 100)}%` }}
                      />
                    </div>
                    <span className="text-xs font-semibold text-gray-500 w-10 text-right">
                      {formatConfidence(alt.confidence)}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div className="grid grid-cols-2 gap-3">
          <button
            onClick={handleShare}
            className="flex items-center justify-center gap-2 bg-primary text-white font-semibold py-3.5 rounded-2xl active:scale-95 transition-transform text-sm"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
            </svg>
            Share Result
          </button>
          <button
            onClick={() => navigate('/diagnose')}
            className="flex items-center justify-center gap-2 bg-white text-primary border-2 border-primary font-semibold py-3.5 rounded-2xl active:scale-95 transition-transform text-sm"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 4v16m8-8H4" />
            </svg>
            New Scan
          </button>
        </div>
      </div>
    </div>
  )
}
