/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './layouts/**/*.html',
    './content/**/*.{html,md}',
    '../../layouts/**/*.html',
    '../../content/**/*.{html,md}',
    '../**/layouts/**/*.html',
    '../**/content/**/*.{html,md}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: 'var(--color-primary, #1a73e8)',
          light: 'var(--color-primary-light, #4285f4)',
          dark: 'var(--color-primary-dark, #1557b0)',
        },
        secondary: {
          DEFAULT: 'var(--color-secondary, #34a853)',
          light: 'var(--color-secondary-light, #46c167)',
          dark: 'var(--color-secondary-dark, #2d8644)',
        },
        accent: 'var(--color-accent, #fbbc05)',

        text: {
          DEFAULT: 'var(--color-text, #ff0000)',
          light: 'var(--color-text-light, #5f6368)',
          muted: 'var(--color-text-muted, #9aa0a6)',
        },
        background: {
          DEFAULT: 'var(--color-background, #ffffff)',
          alt: 'var(--color-background-alt, #f8f9fa)',
          dark: 'var(--color-background-dark, #f1f3f4)',
        },
      },
      backgroundImage: {
        'gradient-primary': 'var(--gradient-primary)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
  // Ensure Tailwind doesn't conflict with the lazy loading and responsive image features
  safelist: ['lazy-load', 'lazy-load-bg', 'lazy-load-video', 'picture', 'source', 'webp', 'srcset'],
};
