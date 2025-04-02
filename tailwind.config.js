/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./layouts/**/*.html",
    "./content/**/*.{html,md}",
    "./themes/**/layouts/**/*.html",
    "./themes/**/content/**/*.{html,md}"
  ],
  theme: {
    extend: {
      // Add any custom theme extensions here
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '100ch', // Wider content area for better readability
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
  // Ensure Tailwind doesn't conflict with the lazy loading and responsive image features
  safelist: [
    'lazy-load',
    'lazy-load-bg',
    'lazy-load-video',
    'picture',
    'source',
    'webp',
    'srcset'
  ]
}
