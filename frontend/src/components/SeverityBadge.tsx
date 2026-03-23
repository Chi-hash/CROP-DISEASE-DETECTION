interface Props {
  severity: string
  size?: 'sm' | 'md'
}

const config: Record<string, { bg: string; text: string; label: string }> = {
  severe: { bg: 'bg-red-100', text: 'text-danger', label: 'Severe' },
  moderate: { bg: 'bg-amber-100', text: 'text-warning', label: 'Moderate' },
  mild: { bg: 'bg-green-100', text: 'text-accent', label: 'Mild' },
  none: { bg: 'bg-green-100', text: 'text-accent', label: 'Healthy' },
}

export default function SeverityBadge({ severity, size = 'md' }: Props) {
  const key = severity.toLowerCase()
  const { bg, text, label } = config[key] ?? config.moderate
  const padding = size === 'sm' ? 'px-2 py-0.5 text-xs' : 'px-3 py-1 text-sm'
  return (
    <span className={`inline-flex items-center rounded-full font-semibold ${bg} ${text} ${padding}`}>
      {label}
    </span>
  )
}
