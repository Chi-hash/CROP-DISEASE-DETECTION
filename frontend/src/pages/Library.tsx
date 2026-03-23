import { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchDiseases, fetchCrops } from '../utils/api'
import type { Disease } from '../types'
import DiseaseCard from '../components/DiseaseCard'
import SeverityBadge from '../components/SeverityBadge'
import TreatmentSection from '../components/TreatmentCard'

export function LibraryDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [disease, setDisease] = useState<Disease | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchDiseases().then(all => {
      const found = all.find(d => d.id === id)
      setDisease(found ?? null)
      setLoading(false)
    })
  }, [id])

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center pb-20">
        <div className="animate-spin w-10 h-10 rounded-full border-4 border-primary border-t-transparent" />
      </div>
    )
  }

  if (!disease) {
    return (
      <div className="min-h-screen bg-background flex flex-col items-center justify-center gap-3 pb-20 px-6">
        <span className="text-5xl">🌿</span>
        <p className="text-gray-500">Disease not found.</p>
        <button onClick={() => navigate('/library')} className="text-primary font-semibold">← Back to Library</button>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background pb-24">
      <div className="bg-primary text-white px-6 pt-10 pb-6">
        <button onClick={() => navigate('/library')} className="flex items-center gap-1 text-white/80 text-sm mb-4">
          <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Disease Library
        </button>
        <h1 className="text-2xl font-bold">{disease.common_name}</h1>
        <p className="text-green-100 italic text-sm mt-0.5">{disease.scientific_name}</p>
        <div className="flex items-center gap-2 mt-3">
          <span className="bg-white/20 text-white text-xs font-medium px-2 py-1 rounded-full">{disease.crop}</span>
          <SeverityBadge severity={disease.severity} size="sm" />
        </div>
      </div>

      <div className="max-w-lg mx-auto px-4 py-5 space-y-4">
        <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-2">Overview</h2>
          <p className="text-sm text-gray-700 leading-relaxed">{disease.description}</p>
        </div>

        <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-2">Causes</h2>
          <p className="text-sm text-gray-700 leading-relaxed">{disease.causes}</p>
        </div>

        <div className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-3">Symptoms</h2>
          <ul className="space-y-2">
            {disease.symptoms.map((s, i) => (
              <li key={i} className="flex gap-2 text-sm text-gray-700">
                <span className="text-warning flex-shrink-0">⚠️</span>
                <span>{s}</span>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h2 className="font-bold text-text-primary mb-3">Treatment & Prevention</h2>
          <TreatmentSection
            organic={disease.treatment.organic}
            chemical={disease.treatment.chemical}
            prevention={disease.treatment.prevention}
          />
        </div>

        <div className="flex flex-wrap gap-2">
          {disease.tags.map(tag => (
            <span key={tag} className="bg-green-50 text-primary text-xs font-medium px-3 py-1 rounded-full border border-green-100">
              #{tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  )
}

export default function Library() {
  const [diseases, setDiseases] = useState<Disease[]>([])
  const [crops, setCrops] = useState<string[]>([])
  const [selectedCrop, setSelectedCrop] = useState<string>('')
  const [search, setSearch] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([fetchDiseases(), fetchCrops()]).then(([d, c]) => {
      setDiseases(d)
      setCrops(c)
      setLoading(false)
    })
  }, [])

  const filtered = diseases.filter(d => {
    if (d.severity.toLowerCase() === 'none') return false  // hide healthy entries
    const matchCrop = !selectedCrop || d.crop === selectedCrop
    const matchSearch = !search || d.common_name.toLowerCase().includes(search.toLowerCase()) || d.crop.toLowerCase().includes(search.toLowerCase())
    return matchCrop && matchSearch
  })

  return (
    <div className="min-h-screen bg-background pb-20">
      <div className="bg-primary text-white px-6 pt-10 pb-5">
        <h1 className="text-2xl font-bold">Disease Library</h1>
        <p className="text-green-100 text-sm mt-1">Browse {diseases.length} crop diseases across {crops.length} crops</p>
      </div>

      <div className="sticky top-0 bg-white border-b border-gray-100 px-4 py-3 z-10 space-y-2">
        <input
          value={search}
          onChange={e => setSearch(e.target.value)}
          placeholder="Search diseases or crops…"
          className="w-full bg-gray-100 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
        />
        <div className="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
          <button
            onClick={() => setSelectedCrop('')}
            className={`flex-shrink-0 px-3 py-1.5 rounded-full text-sm font-medium transition-colors ${!selectedCrop ? 'bg-primary text-white' : 'bg-gray-100 text-gray-600'}`}
          >
            All
          </button>
          {crops.map(crop => (
            <button
              key={crop}
              onClick={() => setSelectedCrop(crop === selectedCrop ? '' : crop)}
              className={`flex-shrink-0 px-3 py-1.5 rounded-full text-sm font-medium transition-colors ${selectedCrop === crop ? 'bg-primary text-white' : 'bg-gray-100 text-gray-600'}`}
            >
              {crop}
            </button>
          ))}
        </div>
      </div>

      <div className="w-full px-4 py-4">
        {loading ? (
          <div className="flex justify-center py-20">
            <div className="animate-spin w-10 h-10 rounded-full border-4 border-primary border-t-transparent" />
          </div>
        ) : filtered.length === 0 ? (
          <div className="text-center py-16 text-gray-400">
            <span className="text-5xl">🌿</span>
            <p className="mt-3">No diseases found matching your search.</p>
          </div>
        ) : (
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
            {filtered.map(d => <DiseaseCard key={d.id} disease={d} />)}
          </div>
        )}
      </div>
    </div>
  )
}
