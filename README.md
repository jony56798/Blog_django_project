# Simple Blog (Django)

Beginner-friendly Django blog with auth, CRUD posts, comments, pagination, and search.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000

## Features
- Register, login, logout
- Create/Edit/Delete posts (author-only)
- Comments on post detail (logged-in)
- Pagination + basic search (?q=keyword)
- Django messages + Bootstrap styling

## Deploy
- Works on free hosts (Render/Railway/Heroku-style).
- Set `SECRET_KEY` in env for production.
