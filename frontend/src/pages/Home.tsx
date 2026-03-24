import { useNavigate } from 'react-router-dom'

const features = [
  { icon: '⚡', title: 'Instant Results', desc: 'Diagnosis in under 10 seconds' },
  { icon: '🎯', title: '>80% Accuracy', desc: 'AI trained on 50,000+ leaf images' },
  { icon: '💊', title: 'Treatment Plans', desc: 'Organic & chemical options' },
  { icon: '📶', title: 'Works on 2G', desc: 'Built for rural connectivity' },
]

const crops = ['🌽 Maize', '🍅 Tomato', '🥔 Potato', '🌾 Rice', '🌿 Cassava', '🫑 Pepper', '🌾 Wheat']

export default function Home() {
  const navigate = useNavigate()

  return (
    <div className="min-h-screen bg-background pb-20">
      {/* Hero */}
      <div className="bg-gradient-to-b from-primary to-primary-light text-white px-6 pt-12 pb-16 relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-4 right-4 text-9xl">🌿</div>
          <div className="absolute bottom-4 left-4 text-6xl">🍃</div>
        </div>
        <div className="relative max-w-lg mx-auto">
          <div className="flex items-center gap-2 mb-4">
            <img src="/leaf-icon.svg" alt="AgriScan" className="w-9 h-9" />
            <h1 className="text-2xl font-bold">AgriScan</h1>
          </div>
          <p className="text-4xl font-extrabold leading-tight mb-3">
            Diagnose Crop Diseases Instantly
          </p>
          <p className="text-green-100 text-base leading-relaxed mb-8">
            Upload a photo of your crop leaf. Get an AI-powered disease diagnosis, treatment plan, and prevention tips in seconds.
          </p>
          <button
            onClick={() => navigate('/diagnose')}
            className="w-full bg-white text-primary font-bold text-lg py-4 rounded-2xl shadow-xl flex items-center justify-center gap-3 active:scale-95 transition-transform"
          >
            <svg className="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
              <path strokeLinecap="round" strokeLinejoin="round" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            Scan Your Crop Now
          </button>
        </div>
      </div>

      <div className="w-full px-4 lg:px-[100px]">
        {/* Stats */}
        <div className="grid grid-cols-3 gap-3 mt-[50px] mb-6">
          {[
            { num: '500M+', label: 'Farmers Targeted' },
            { num: '41+', label: 'Diseases Detected' },
            { num: '14', label: 'Crops Covered' },
          ].map(({ num, label }) => (
            <div key={label} className="bg-white rounded-2xl p-3 text-center shadow-sm border border-gray-100">
              <p className="text-xl font-extrabold text-primary">{num}</p>
              <p className="text-xs text-gray-500 mt-0.5 leading-tight">{label}</p>
            </div>
          ))}
        </div>

      </div>

      {/* Features - full width so grid-cols-4 has room */}
      <div className="w-full px-4 lg:px-[100px] mb-6">
        <h2 className="text-lg font-bold text-text-primary mb-3">Why AgriScan?</h2>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
          {features.map(({ icon, title, desc }) => (
            <div key={title} className="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
              <span className="text-2xl">{icon}</span>
              <h3 className="font-semibold text-text-primary mt-2 text-sm">{title}</h3>
              <p className="text-xs text-gray-500 mt-1">{desc}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="w-full px-4 lg:px-[100px]">

        {/* Supported Crops */}
        <h2 className="text-lg font-bold text-text-primary mb-3">Supported Crops</h2>
        <div className="flex flex-wrap gap-2 mb-6">
          {crops.map(crop => (
            <span key={crop} className="bg-green-50 text-primary text-sm font-medium px-3 py-1.5 rounded-full border border-green-100">
              {crop}
            </span>
          ))}
        </div>

        {/* How it works */}
        <h2 className="text-lg font-bold text-text-primary mb-3">How It Works</h2>
        <div className="space-y-3 mb-6">
          {[
            { step: '1', title: 'Photograph the leaf', desc: 'Take a clear, close-up photo of the affected plant leaf' },
            { step: '2', title: 'Upload to AgriScan', desc: 'Tap "Scan Your Crop" and select your photo or take one now' },
            { step: '3', title: 'Get your diagnosis', desc: 'Receive disease name, confidence score, and treatment plan in seconds' },
          ].map(({ step, title, desc }) => (
            <div key={step} className="flex gap-4 bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
              <div className="flex-shrink-0 w-10 h-10 rounded-full bg-primary text-white font-bold flex items-center justify-center text-sm">
                {step}
              </div>
              <div>
                <h3 className="font-semibold text-text-primary text-sm">{title}</h3>
                <p className="text-xs text-gray-500 mt-0.5">{desc}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Mission */}
        <div className="bg-primary/5 border border-primary/10 rounded-2xl p-5 text-center mb-4">
          <p className="text-sm text-gray-700 leading-relaxed italic">
            "Democratizing agricultural expertise for the 500 million smallholder farmers who currently have no access to agronomists."
          </p>
          <p className="text-xs text-primary font-semibold mt-2">AgriScan Mission</p>
        </div>
      </div>
    </div>
  )
}
