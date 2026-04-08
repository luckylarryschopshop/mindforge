# Mindforge

Idea tracker web app

## Run

```bash
docker compose up -d
# Open http://127.0.0.1:PORT
```

## API

  - GET /api/mindforge — list all items
  - POST /api/mindforge — add item (send JSON body)
  - PUT /api/mindforge/{id} — update item (send JSON body)
  - DELETE /api/mindforge/{id} — delete item
  - GET /api/mindforge/search?q=term — search items
