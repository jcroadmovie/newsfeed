// React hooks used in this component
import { useEffect, useState } from 'react';

// Helper to display relative publish time
function timeAgo(dateStr) {
  const diff = Math.floor((Date.now() - new Date(dateStr)) / 1000); // seconds ago
  if (diff < 60) return `${diff} sec ago`;
  const m = Math.floor(diff / 60);
  if (m < 60) return `${m} min ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h} hr ago`;
  const d = Math.floor(h / 24);
  return `${d} day${d > 1 ? 's' : ''} ago`;
}

export default function Home() {
  // list of news items
  const [items, setItems] = useState([]);
  // text shown in the toast notification
  const [toast, setToast] = useState('');

  // Fetch initial data and open SSE connection on mount
  useEffect(() => {
    fetch('http://localhost:8000/api/newsfeed/')
      .then(res => res.json())           // parse JSON response
      .then(data => setItems(data));     // populate initial list

    const es = new EventSource('http://localhost:8000/api/newsfeed/stream/');
    es.onmessage = evt => {
      const item = JSON.parse(evt.data);       // parse SSE event data
      setItems(prev => [item, ...prev]);       // prepend new item
      setToast('New item available');          // show toast
      setTimeout(() => setToast(''), 3000);    // hide toast after delay
    };

    return () => es.close();                   // cleanup on unmount
  }, []);

  // Render list and toast UI
  return (
    <div>
      <header>Newsfeed</header>
      {toast && <div className="toast">{toast}</div>}
      <ul className="news-list">
        {items.map((item, idx) => (
          <li key={idx} className="news-item">
            <a href={item.link} target="_blank" rel="noopener noreferrer">
              {item.title}
            </a>
            <p>{timeAgo(item.published)}</p>
            <div dangerouslySetInnerHTML={{ __html: item.summary }} />
          </li>
        ))}
      </ul>
    </div>
  );
}
