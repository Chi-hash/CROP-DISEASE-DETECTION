interface Props {
  title: string
  icon: React.ReactNode
  steps: string[]
  accentClass: string
}

function TreatmentCard({ title, icon, steps, accentClass }: Props) {
  return (
    <div className="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
      <div className={`flex items-center gap-2 px-4 py-3 ${accentClass}`}>
        <span className="text-xl">{icon}</span>
        <h3 className="font-semibold text-sm">{title}</h3>
      </div>
      <ul className="px-4 py-3 space-y-2">
        {steps.map((step, i) => (
          <li key={i} className="flex gap-3 text-sm text-gray-700">
            <span className="flex-shrink-0 w-6 h-6 rounded-full bg-gray-100 flex items-center justify-center text-xs font-bold text-gray-500">
              {i + 1}
            </span>
            <span>{step}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}

interface TreatmentSectionProps {
  organic: string[]
  chemical: string[]
  prevention: string[]
}

export default function TreatmentSection({ organic, chemical, prevention }: TreatmentSectionProps) {
  return (
    <div className="space-y-3">
      <TreatmentCard title="Organic Treatment" icon="🌿" steps={organic} accentClass="bg-green-50 text-primary" />
      <TreatmentCard title="Chemical Treatment" icon="⚗️" steps={chemical} accentClass="bg-blue-50 text-blue-700" />
      <TreatmentCard title="Prevention Tips" icon="🛡️" steps={prevention} accentClass="bg-amber-50 text-amber-700" />
    </div>
  )
}
