# Notes API - FastAPI

A REST API for managing notes with CRUD operations, built with FastAPI. Features a clean service-oriented architecture with async endpoints and background tasks.

## Features

- **CRUD Operations** - Create, read, update, delete notes
- **Services Layer** - Separated business logic from HTTP handling
- **Async Endpoints** - Concurrent request handling
- **Background Tasks** - Non-blocking logging operations
- **Pagination & Filtering** - Query notes with limits and title search
- **Data Validation** - Pydantic schemas for all requests/responses
- **In-Memory Storage** - Fast, simple data persistence

## Project Structure

```
src/
├── main.py              # FastAPI app, lifespan, root endpoint
├── models/
│   └── note.py          # Pydantic schemas (NoteCreate, NoteUpdate, NoteResponse)
├── routes/
│   └── notes.py         # HTTP endpoints
├── services/
│   └── note_service.py  # Business logic layer
├── storage/
│   └── memory.py        # Data access layer with Note dataclass
└── tasks/
    └── background.py    # Background task functions
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python -m src.main
```

Visit `http://localhost:8000/docs` for interactive API docs.

## API Endpoints

| Method | Endpoint      | Purpose         |
| ------ | ------------- | --------------- |
| POST   | `/notes`      | Create note     |
| GET    | `/notes`      | Get all notes   |
| GET    | `/notes/{id}` | Get single note |
| PUT    | `/notes/{id}` | Update note     |
| DELETE | `/notes/{id}` | Delete note     |

## Query Parameters

- `limit` (1-100, default 10) - Pagination limit
- `skip` (default 0) - Pagination offset
- `title` (optional) - Filter by title

## Architecture

### Services Layer

Business logic separated from HTTP handling for better testability and reusability.

### Async Endpoints

`GET /notes` and `PUT /notes/{id}` are async for efficient concurrent request handling.

### Background Tasks

Create/update/delete operations log asynchronously without blocking responses.
