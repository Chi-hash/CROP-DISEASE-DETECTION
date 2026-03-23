import { NavLink } from 'react-router-dom'

const navItems = [
  { to: '/', label: 'Home', icon: HomeIcon },
  { to: '/diagnose', label: 'Diagnose', icon: ScanIcon },
  { to: '/library', label: 'Library', icon: BookIcon },
  { to: '/history', label: 'History', icon: HistoryIcon },
  { to: '/about', label: 'About', icon: InfoIcon },
]

function HomeIcon() {
  return (
    <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
    </svg>
  )
}

function ScanIcon() {
  return (
    <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
      <path strokeLinecap="round" strokeLinejoin="round" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
    </svg>
  )
}

function BookIcon() {
  return (
    <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
    </svg>
  )
}

function HistoryIcon() {
  return (
    <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
  )
}

function InfoIcon() {
  return (
    <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
  )
}

export default function BottomNav() {
  return (
    <nav className="
      fixed z-50 bg-white
      bottom-0 left-0 right-0 border-t border-gray-200
      md:bottom-auto md:top-0 md:border-t-0 md:border-b md:border-gray-200 md:shadow-sm
    ">
      <div className="max-w-5xl mx-auto flex items-center md:justify-between md:px-8 justify-around">
        {/* Logo - only visible on desktop */}
        <NavLink to="/" className="hidden md:flex items-center gap-2 text-primary font-bold text-lg py-4">
          <span className="text-2xl">🌱</span>
          CropCare AI
        </NavLink>

        {/* Nav links */}
        <div className="flex items-center justify-around md:justify-end md:gap-1 w-full md:w-auto">
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              end={to === '/'}
              className={({ isActive }) =>
                `flex flex-col md:flex-row items-center justify-center gap-0 md:gap-2
                 py-2 px-3 md:px-4 md:py-3 min-w-[44px] min-h-[56px] md:min-h-0
                 rounded-xl transition-colors font-medium
                 ${isActive
                   ? 'text-primary md:bg-green-50'
                   : 'text-gray-400 hover:text-gray-600 md:hover:bg-gray-50'
                 }`
              }
            >
              <Icon />
              <span className="text-xs md:text-sm mt-1 md:mt-0">{label}</span>
            </NavLink>
          ))}
        </div>
      </div>
    </nav>
  )
}
