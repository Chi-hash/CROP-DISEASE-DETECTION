/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#1A5C38',
        'primary-light': '#236b43',
        accent: '#4CAF74',
        warning: '#F59E0B',
        danger: '#DC2626',
        background: '#F9FAF8',
        'text-primary': '#1A1A1A',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
