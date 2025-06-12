# Newsfeed Prototype

This repository contains a simple prototype demonstrating how to serve a newsfeed
from a Django REST API and display it with a Next.js front‑end.

The backend fetches entries from an external RSS feed and exposes them through
`/api/newsfeed/`. The frontend consumes this endpoint and renders the list.

### prototype sample image

![newsfeed_screenshot](https://github.com/user-attachments/assets/d58ce17e-7523-4a5f-8124-917a4a339ca1)

## Backend (Django)

The Django project lives in `backend/`. Dependencies are listed in
`backend/requirements.txt` (Django, Django REST framework and feedparser).

Run migrations and start the server:

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Frontend (Next.js)

The Next.js app resides in `frontend/`. After installing dependencies you can
start the development server:

```bash
cd frontend
npm install
npm run dev
```

The page at `http://localhost:3000` will request RSS entries from the backend
running at `http://localhost:8000`.
