# Mindforge

Idea tracker with web UI.

## Run

```bash
docker compose up -d
# Open http://localhost:3003
```

## Features

- Add, search, delete ideas
- Tag support
- Persistent storage
- Dark theme

## API

- GET /api/ideas
- POST /api/ideas
- DELETE /api/ideas/:id
- GET /api/ideas/search?q=term