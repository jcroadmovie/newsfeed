// Global CSS import to apply styles across the app
import '../styles/globals.css';

// Next.js custom App component; renders each page
export default function MyApp({ Component, pageProps }) {
  // simply pass through to the actual page component
  return <Component {...pageProps} />;
}
