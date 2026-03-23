interface Props {
  confidence: number
}

export default function ConfidenceGauge({ confidence }: Props) {
  const pct = Math.round(confidence * 100)

  let color = '#DC2626'
  let label = 'Low'
  if (pct >= 80) { color = '#4CAF74'; label = 'High' }
  else if (pct >= 50) { color = '#F59E0B'; label = 'Medium' }

  const radius = 40
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (pct / 100) * circumference

  return (
    <div className="flex flex-col items-center">
      <div className="relative w-28 h-28">
        <svg className="w-full h-full -rotate-90" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r={radius} fill="none" stroke="#E5E7EB" strokeWidth="10" />
          <circle
            cx="50"
            cy="50"
            r={radius}
            fill="none"
            stroke={color}
            strokeWidth="10"
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            strokeLinecap="round"
            style={{ transition: 'stroke-dashoffset 1s ease-in-out' }}
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-2xl font-bold text-text-primary">{pct}%</span>
          <span className="text-xs text-gray-500 font-medium">{label}</span>
        </div>
      </div>
      <span className="mt-1 text-sm text-gray-600 font-medium">Confidence</span>
    </div>
  )
}
