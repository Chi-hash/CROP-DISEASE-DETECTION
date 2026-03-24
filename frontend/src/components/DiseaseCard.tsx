import { useNavigate } from 'react-router-dom'
import { useState } from 'react'
import type { Disease } from '../types'
import SeverityBadge from './SeverityBadge'
import { getAssetUrl } from '../utils/api'

interface Props {
  disease: Disease
}

const cropEmoji: Record<string, string> = {
  Tomato: '🍅',
  Maize: '🌽',
  Potato: '🥔',
  Rice: '🌾',
  Cassava: '🌿',
  Pepper: '🫑',
  Wheat: '🌾',
}

export default function DiseaseCard({ disease }: Props) {
  const navigate = useNavigate()
  const [imgError, setImgError] = useState(false)
  const emoji = cropEmoji[disease.crop] ?? '🌿'

  return (
    <button
      onClick={() => navigate(`/library/${disease.id}`)}
      className="w-full text-left bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden hover:shadow-md active:scale-95 transition-all"
    >
      {/* Image - shorter on mobile, taller on desktop */}
      <div className="h-24 lg:h-32 bg-gradient-to-br from-primary to-accent flex items-center justify-center relative overflow-hidden">
        {!imgError ? (
          <img
            src={getAssetUrl(disease.image_url)}
            alt={disease.common_name}
            className="w-full h-full object-cover"
            onError={() => setImgError(true)}
          />
        ) : (
          <div className="flex flex-col items-center justify-center gap-1">
            <span className="text-4xl">{emoji}</span>
            <span className="text-white text-xs font-medium opacity-80">{disease.crop}</span>
          </div>
        )}
      </div>

      {/* Content - tighter padding on mobile */}
      <div className="p-3 lg:p-4">
        {/* Name stacked above badge on mobile, side-by-side on lg+ */}
        <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between lg:gap-2">
          <h3 className="font-semibold text-text-primary text-sm leading-tight">{disease.common_name}</h3>
          <div className="mt-1 lg:mt-0 flex-shrink-0">
            <SeverityBadge severity={disease.severity} size="sm" />
          </div>
        </div>

        {/* Scientific name - hidden on mobile, visible on md+ */}
        <p className="hidden md:block text-xs text-gray-500 italic mt-0.5">{disease.scientific_name}</p>

        {/* Tags */}
        <div className="mt-2 flex items-center gap-1 flex-wrap">
          <span className="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded-full font-medium">
            {disease.crop}
          </span>
          {disease.tags.slice(0, 1).map(t => (
            <span key={t} className="text-xs bg-green-50 text-primary px-2 py-0.5 rounded-full font-medium">
              {t}
            </span>
          ))}
        </div>
      </div>
    </button>
  )
}
