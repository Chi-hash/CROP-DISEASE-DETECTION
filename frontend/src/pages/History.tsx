import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { getHistory, clearHistory } from '../utils/storage'
import type { DiagnosisRecord } from '../types'
import SeverityBadge from '../components/SeverityBadge'
import { formatConfidence } from '../utils/imageUtils'

export default function History() {
  const navigate = useNavigate()
  const [records, setRecords] = useState<DiagnosisRecord[]>([])

  useEffect(() => {
    setRecords(getHistory())
  }, [])

  function handleClear() {
    if (confirm('Clear all diagnosis history? This cannot be undone.')) {
      clearHistory()
      setRecords([])
    }
  }

  function handleView(record: DiagnosisRecord) {
    navigate('/results', { state: { result: record.result, preview: record.image_preview } })
  }

  function formatDate(iso: string) {
    return new Date(iso).toLocaleDateString('en-GB', {
      day: 'numeric', month: 'short', year: 'numeric',
      hour: '2-digit', minute: '2-digit',
    })
  }

  return (
    <div className="min-h-screen bg-background pb-20">
      <div className="bg-primary text-white px-6 pt-10 pb-5 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">My Diagnoses</h1>
          <p className="text-green-100 text-sm mt-1">{records.length} of last 10 diagnoses</p>
        </div>
        {records.length > 0 && (
          <button onClick={handleClear} className="text-white/70 text-sm hover:text-white">
            Clear All
          </button>
        )}
      </div>

      <div className="max-w-4xl mx-auto px-4 py-4">
        {records.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-20 gap-4 text-center">
            <span className="text-6xl">🌿</span>
            <h2 className="text-xl font-bold text-text-primary">No Diagnoses Yet</h2>
            <p className="text-gray-500 text-sm max-w-xs">
              Your last 10 crop diagnoses will appear here. Scan your first crop to get started!
            </p>
            <button
              onClick={() => navigate('/diagnose')}
              className="bg-primary text-white font-semibold px-8 py-3 rounded-2xl mt-2 active:scale-95 transition-transform"
            >
              Scan a Crop
            </button>
          </div>
        ) : (
          <div className="space-y-3">
            {records.map((record) => (
              <button
                key={record.id}
                onClick={() => handleView(record)}
                className="w-full text-left bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden flex gap-0 active:scale-95 transition-all hover:shadow-md"
              >
                <div className="w-24 h-24 flex-shrink-0 bg-gray-100 overflow-hidden">
                  {record.image_preview ? (
                    <img
                      src={record.image_preview}
                      alt={record.disease_name}
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center text-3xl">🌿</div>
                  )}
                </div>
                <div className="p-3 flex-1 min-w-0">
                  <div className="flex items-start justify-between gap-2">
                    <h3 className="font-semibold text-text-primary text-sm truncate">{record.disease_name}</h3>
                    <SeverityBadge severity={record.severity} size="sm" />
                  </div>
                  <p className="text-xs text-gray-500 mt-0.5">{record.crop}</p>
                  <div className="flex items-center justify-between mt-2">
                    <span className="text-xs text-gray-400">{formatDate(record.date)}</span>
                    <span className="text-xs font-semibold text-primary">{formatConfidence(record.confidence)}</span>
                  </div>
                </div>
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
