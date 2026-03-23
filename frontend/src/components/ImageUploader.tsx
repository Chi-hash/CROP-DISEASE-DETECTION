import { useRef, useState } from 'react'

interface Props {
  onImageSelected: (file: File, preview: string) => void
}

export default function ImageUploader({ onImageSelected }: Props) {
  const fileInputRef = useRef<HTMLInputElement>(null)
  const cameraInputRef = useRef<HTMLInputElement>(null)
  const [dragOver, setDragOver] = useState(false)

  function handleFile(file: File) {
    if (!file.type.startsWith('image/')) {
      alert('Please select an image file (JPEG, PNG, or WEBP).')
      return
    }
    const url = URL.createObjectURL(file)
    onImageSelected(file, url)
  }

  function onFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]
    if (file) handleFile(file)
  }

  function onDrop(e: React.DragEvent) {
    e.preventDefault()
    setDragOver(false)
    const file = e.dataTransfer.files?.[0]
    if (file) handleFile(file)
  }

  return (
    <div className="space-y-4">
      <div
        onDrop={onDrop}
        onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
        onDragLeave={() => setDragOver(false)}
        className={`border-2 border-dashed rounded-3xl p-8 flex flex-col items-center justify-center gap-3 transition-colors cursor-pointer ${
          dragOver ? 'border-primary bg-green-50' : 'border-gray-300 bg-gray-50'
        }`}
        onClick={() => fileInputRef.current?.click()}
      >
        <div className="w-20 h-20 rounded-full bg-primary/10 flex items-center justify-center">
          <svg className="w-10 h-10 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
          </svg>
        </div>
        <div className="text-center">
          <p className="font-semibold text-text-primary">Drop your leaf photo here</p>
          <p className="text-sm text-gray-500 mt-1">or tap to browse your gallery</p>
        </div>
        <input ref={fileInputRef} type="file" accept="image/*" className="hidden" onChange={onFileChange} />
      </div>

      <div className="relative flex items-center">
        <div className="flex-grow border-t border-gray-200" />
        <span className="mx-3 text-sm text-gray-400 font-medium">or</span>
        <div className="flex-grow border-t border-gray-200" />
      </div>

      <button
        onClick={() => cameraInputRef.current?.click()}
        className="w-full flex items-center justify-center gap-3 py-4 rounded-2xl bg-primary text-white font-semibold text-base shadow-lg active:scale-95 transition-transform"
      >
        <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
          <path strokeLinecap="round" strokeLinejoin="round" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        Take Photo with Camera
      </button>
      <input ref={cameraInputRef} type="file" accept="image/*" capture="environment" className="hidden" onChange={onFileChange} />

      <p className="text-center text-xs text-gray-400">
        Supported formats: JPEG, PNG, WEBP · Images compressed automatically
      </p>
    </div>
  )
}
