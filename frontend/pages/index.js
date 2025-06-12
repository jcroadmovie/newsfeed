import { useEffect, useState } from 'react';

export default function Home() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/newsfeed/')
      .then(res => res.json())
      .then(data => setItems(data));
  }, []);

  return (
    <div>
      <h1>Newsfeed</h1>
      <ul>
        {items.map((item, idx) => (
          <li key={idx}>
            <a href={item.link} target="_blank" rel="noopener noreferrer">
              {item.title}
            </a>
            <p>{item.published}</p>
            <div dangerouslySetInnerHTML={{ __html: item.summary }} />
          </li>
        ))}
      </ul>
    </div>
  );
}
