import { useEffect, useState } from 'react';

function timeAgo(dateStr) {
  const diff = Math.floor((Date.now() - new Date(dateStr)) / 1000);
  if (diff < 60) return `${diff} sec ago`;
  const m = Math.floor(diff / 60);
  if (m < 60) return `${m} min ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h} hr ago`;
  const d = Math.floor(h / 24);
  return `${d} day${d > 1 ? 's' : ''} ago`;
}

export default function Home() {
  const [items, setItems] = useState([]);
  const [toast, setToast] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/api/newsfeed/')
      .then(res => res.json())
      .then(data => setItems(data));

    const es = new EventSource('http://localhost:8000/api/newsfeed/stream/');
    es.onmessage = evt => {
      const item = JSON.parse(evt.data);
      setItems(prev => [item, ...prev]);
      setToast('New item available');
      setTimeout(() => setToast(''), 3000);
    };

    return () => es.close();
  }, []);

  return (
    <div>
      <h1>Newsfeed</h1>
      {toast && <div style={{ background: '#333', color: '#fff', padding: '10px' }}>{toast}</div>}
      <ul>
        {items.map((item, idx) => (
          <li key={idx}>
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
