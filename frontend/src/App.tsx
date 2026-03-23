import { BrowserRouter, Routes, Route } from 'react-router-dom'
import BottomNav from './components/BottomNav'
import Home from './pages/Home'
import Diagnose from './pages/Diagnose'
import Results from './pages/Results'
import Library, { LibraryDetail } from './pages/Library'
import History from './pages/History'
import About from './pages/About'

export default function App() {
  return (
    <BrowserRouter>
      <div className="font-sans bg-background min-h-screen md:pt-[65px]">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/diagnose" element={<Diagnose />} />
          <Route path="/results" element={<Results />} />
          <Route path="/library" element={<Library />} />
          <Route path="/library/:id" element={<LibraryDetail />} />
          <Route path="/history" element={<History />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <BottomNav />
      </div>
    </BrowserRouter>
  )
}
