export default function About() {
  return (
    <div className="min-h-screen bg-background pb-20">
      <div className="bg-primary text-white px-6 pt-10 pb-8 text-center">
        <span className="text-5xl">🌱</span>
        <h1 className="text-2xl font-bold mt-3">CropCare AI</h1>
        <p className="text-green-100 text-sm mt-1">Version 1.0 · Hackathon Edition · March 2026</p>
      </div>

      <div className="max-w-lg mx-auto px-4 py-6 space-y-4">
        <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-2">Our Mission</h2>
          <p className="text-sm text-gray-700 leading-relaxed">
            CropCare AI democratises agricultural disease diagnosis for the 500 million+ smallholder
            farmers globally who currently lack access to agronomists. We reduce crop losses by
            enabling early, accurate, and affordable disease detection using nothing but a smartphone
            camera.
          </p>
        </div>

        <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-3">The Problem We Solve</h2>
          <div className="space-y-3">
            {[
              { icon: '📍', title: 'Access Gap', desc: 'Farmers in rural areas have no access to trained agronomists' },
              { icon: '⏱️', title: 'Speed Gap', desc: 'By the time diagnosis arrives, disease spread may be irreversible' },
              { icon: '💰', title: 'Cost Gap', desc: 'Professional consultations are unaffordable for farmers earning under $2/day' },
              { icon: '📚', title: 'Knowledge Gap', desc: 'Misidentified diseases lead to wrong treatments, worsening crop health' },
            ].map(({ icon, title, desc }) => (
              <div key={title} className="flex gap-3">
                <span className="text-xl flex-shrink-0">{icon}</span>
                <div>
                  <p className="font-semibold text-sm text-text-primary">{title}</p>
                  <p className="text-xs text-gray-600 mt-0.5">{desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-3">Technology Stack</h2>
          <div className="space-y-2">
            {[
              { label: 'Frontend', value: 'React 18 + TypeScript + TailwindCSS' },
              { label: 'Backend', value: 'Python FastAPI + Uvicorn' },
              { label: 'AI Model', value: 'CNN (PlantVillage) / Plant.id API' },
              { label: 'Deployment', value: 'Vercel (frontend) + Render (backend)' },
            ].map(({ label, value }) => (
              <div key={label} className="flex justify-between text-sm py-1.5 border-b border-gray-50 last:border-0">
                <span className="text-gray-500 font-medium">{label}</span>
                <span className="text-text-primary font-semibold text-right max-w-[55%]">{value}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-3">Impact Metrics</h2>
          <div className="grid grid-cols-2 gap-3">
            {[
              { num: '41+', label: 'Diseases Detected' },
              { num: '14', label: 'Crops Covered' },
              { num: '<10s', label: 'Diagnosis Time' },
              { num: '>80%', label: 'Accuracy' },
            ].map(({ num, label }) => (
              <div key={label} className="text-center py-3 bg-green-50 rounded-xl">
                <p className="text-2xl font-extrabold text-primary">{num}</p>
                <p className="text-xs text-gray-500 mt-0.5">{label}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-100">
          <h2 className="font-bold text-text-primary mb-2">Target Regions</h2>
          <div className="flex flex-wrap gap-2">
            {['Sub-Saharan Africa', 'South Asia', 'Southeast Asia', 'West Africa', 'East Africa'].map(r => (
              <span key={r} className="bg-primary/10 text-primary text-xs font-medium px-3 py-1.5 rounded-full">{r}</span>
            ))}
          </div>
        </div>

        <div className="text-center py-4">
          <p className="text-sm text-gray-400 italic">"Every farmer deserves access to world-class agricultural intelligence."</p>
          <p className="text-xs text-primary font-semibold mt-1">CropCare AI Team</p>
        </div>
      </div>
    </div>
  )
}
