# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Tech Stack

### Frontend
- Framework: Vue 3 with JavaScript
- Build Tool: Vite
- Routing: Vue Router
- Data Fetching: Axios
- State Management: Vue ref (Composition API)
- UI Framework: Vuetify
- Charts: Chart.js
- HTTP Client: Custom fetch wrapper with credentials

### Backend
- Framework: FastAPI
- ORM: SQLAlchemy
- Database: MySQL
- API Style: RESTful JSON
- Authentication: Session-based with Redis cache
- Logging: Loguru with OS-level and file logging

## Development Commands

### Frontend
```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint
npm run lint
```

### Backend
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload

# Run with specific host/port
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest

# Run single test
pytest tests/test_specific.py::test_function_name

# Run with coverage
pytest --cov=app tests/
```

### Database
```bash
# Create migration
alembic revision --autogenerate -m "migration message"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Architecture Overview

### Frontend Architecture
- Vue 3 Composition API with `ref` for reactive state
- Custom fetch wrapper handles credentials and authentication
- Vuetify components for consistent UI
- Chart.js for data visualization
- Axios for HTTP requests (alongside custom fetch wrapper)

### Backend Architecture
- FastAPI application with SQLAlchemy ORM models
- Session-based authentication stored in Redis for performance
- MySQL database for persistent storage
- Loguru for unified logging (console, file, and OS-level logs)
- RESTful API endpoints returning JSON

### Authentication Flow
- Session-based authentication (not JWT)
- Sessions cached in Redis for fast lookup
- Frontend sends credentials with each request via custom fetch wrapper
- Backend validates session from Redis cache

### Database Layer
- SQLAlchemy ORM models define schema
- MySQL as the primary database
- Alembic handles database migrations
- Redis used exclusively for session storage and caching

### API Communication
- Frontend makes requests using custom fetch wrapper (with credentials) or Axios
- Backend returns JSON responses
- RESTful conventions for endpoint design
- CORS configured to allow frontend origin

## Key Integration Points

### Frontend-Backend Communication
- Custom fetch wrapper automatically includes credentials
- Axios requests should also be configured for credentials if used
- Base URL configuration should point to FastAPI backend

### Session Management
- Backend creates session on successful authentication
- Session ID stored in Redis with expiration
- Frontend stores session cookie
- Custom fetch wrapper ensures cookie sent with each request

### Logging Strategy
- Backend uses Loguru for all logging
- Three logging targets: console (development), file (persistent), OS-level (system integration)
- Frontend errors should be logged and optionally sent to backend for tracking
