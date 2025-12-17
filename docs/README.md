# Project Documentation

This document explains the MediPredict Lite project structure, naming conventions, and technology choices.

## Table of Contents

- [Folder Structure](#folder-structure)
- [Naming Conventions](#naming-conventions)
- [Tech Stack Choices](#tech-stack-choices)
- [Development Workflow](#development-workflow)

## Folder Structure

```
ai-coding/
├── client/                        # Frontend application (Vue 3)
│   ├── src/
│   │   ├── components/           # Vue components
│   │   ├── assets/              # Static assets (images, fonts)
│   │   ├── App.vue              # Root component
│   │   └── main.ts              # Application entry point
│   ├── public/                   # Public static files
│   ├── package.json              # Node.js dependencies
│   └── vite.config.ts           # Vite configuration
│
├── server/                        # Backend application (FastAPI)
│   ├── pyproject.toml            # Poetry project configuration
│   ├── poetry.lock               # Poetry lock file
│   └── (application code)        # Backend source code (to be created)
│
├── docs/                          # Project documentation
│   ├── features/                 # Feature specifications
│   │   └── DISEASE_RISK_ANALYSIS.md
│   ├── patterns/                 # Architectural patterns
│   │   └── AI_INFERENCE_SERVICE.md
│   └── README.md                 # This file
│
├── docker-compose.yml             # Docker services configuration
├── CLAUDE.md                      # Root context file for AI agents
├── README.md                      # Project setup guide
└── SETUP_COMMANDS.md             # Detailed setup instructions
```

### Directory Purposes

- **`client/`**: Frontend Vue 3 application with TypeScript, Vuetify, and Chart.js
- **`server/`**: Backend FastAPI application with SQLAlchemy, MySQL, and Redis
- **`docs/`**: Project documentation including features and patterns

## Naming Conventions

### File Naming

#### Frontend (Vue/TypeScript)
- **Components**: PascalCase (e.g., `HelloWorld.vue`, `DiseaseRiskCard.vue`)
- **Utilities/Helpers**: camelCase (e.g., `apiClient.ts`, `dateUtils.ts`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `API_BASE_URL.ts`)
- **Types/Interfaces**: PascalCase with `.ts` extension (e.g., `UserTypes.ts`, `ApiResponse.ts`)

#### Backend (Python)
- **Modules**: snake_case (e.g., `user_service.py`, `auth_utils.py`)
- **Classes**: PascalCase (e.g., `UserService`, `DatabaseConnection`)
- **Functions**: snake_case (e.g., `get_user_by_id`, `validate_session`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`)

#### Database
- **Tables**: snake_case, plural (e.g., `users`, `disease_risk_scores`)
- **Columns**: snake_case (e.g., `user_id`, `created_at`)
- **Indexes**: `idx_<table>_<column(s)>` (e.g., `idx_users_email`)

### Code Organization

#### Frontend Structure
```
client/src/
├── components/          # Reusable Vue components
│   ├── common/         # Common UI components (buttons, cards)
│   └── features/       # Feature-specific components
├── views/              # Page-level components (routes)
├── composables/        # Vue Composition API composables
├── services/           # API service layer
├── stores/             # Pinia state management (if used)
├── types/              # TypeScript type definitions
└── utils/              # Utility functions
```

#### Backend Structure
```
server/
├── app/
│   ├── api/            # API route handlers
│   │   └── v1/         # API versioning
│   ├── core/           # Core configuration (config, security)
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic layer
│   ├── utils/           # Utility functions
│   └── main.py         # FastAPI application entry point
├── tests/              # Test files
└── alembic/            # Database migrations
```

## Tech Stack Choices

### Frontend Stack

#### Vue 3 with Composition API
**Why**: 
- Modern reactive framework with excellent TypeScript support
- Composition API provides better code organization and reusability
- Strong ecosystem and community support
- Lightweight and performant

#### Vite
**Why**:
- Fast development server with HMR (Hot Module Replacement)
- Optimized production builds
- Native ES modules support
- Better developer experience than Webpack

#### TypeScript
**Why**:
- Type safety reduces runtime errors
- Better IDE support and autocomplete
- Self-documenting code through types
- Easier refactoring and maintenance

#### Vuetify
**Why**:
- Material Design component library
- Consistent UI/UX out of the box
- Comprehensive component set
- Good TypeScript support

#### Chart.js
**Why**:
- Simple API for data visualization
- Good performance with large datasets
- Responsive and customizable
- Well-maintained library

#### Axios + Custom Fetch Wrapper
**Why**:
- Axios provides interceptors and better error handling
- Custom fetch wrapper ensures credentials are always included
- Consistent API communication pattern
- Easy to mock for testing

### Backend Stack

#### FastAPI
**Why**:
- High performance (comparable to Node.js and Go)
- Automatic API documentation (OpenAPI/Swagger)
- Built-in data validation with Pydantic
- Modern Python async/await support
- Type hints throughout

#### SQLAlchemy
**Why**:
- Mature and widely-used ORM
- Excellent query builder
- Database-agnostic (can switch databases)
- Alembic integration for migrations
- Good performance with connection pooling

#### MySQL 8.0
**Why**:
- Reliable and battle-tested database
- Good performance for relational data
- JSON support for flexible schemas
- Strong ACID compliance
- Wide hosting support

#### Redis 7
**Why**:
- Fast in-memory data store
- Perfect for session storage
- Low latency for authentication checks
- Simple key-value operations
- Pub/sub capabilities for future features

#### Loguru
**Why**:
- Simple and powerful logging
- Better than standard library logging
- Automatic log rotation
- Structured logging support
- Easy configuration

#### Poetry
**Why**:
- Modern Python dependency management
- Lock file ensures reproducible builds
- Better dependency resolution than pip
- Integrated virtual environment management
- Clean project structure

### Infrastructure

#### Docker Compose
**Why**:
- Consistent development environment
- Easy service orchestration
- Isolated dependencies
- Reproducible setup across machines
- Simple service management

#### Adminer
**Why**:
- Lightweight database management tool
- No installation required (Docker)
- Supports MySQL, PostgreSQL, and more
- Simple web interface
- Useful for development and debugging

### Architecture Patterns

#### Service Layer Pattern
**Why**: 
- Separates business logic from API routes
- Makes code testable and reusable
- Prevents blocking in async routes
- See `docs/patterns/AI_INFERENCE_SERVICE.md`

#### Session-Based Authentication
**Why**:
- Simpler than JWT for server-side apps
- Easy to invalidate sessions
- Redis provides fast session lookup
- Secure with HTTP-only cookies

#### RESTful API Design
**Why**:
- Standard and predictable API structure
- Easy to understand and document
- Works well with FastAPI's automatic docs
- Familiar to most developers

## Development Workflow

### Initial Setup
1. Start Docker services: `docker compose up -d`
2. Setup frontend: Follow `SETUP_COMMANDS.md` frontend section
3. Setup backend: Follow `SETUP_COMMANDS.md` backend section

### Daily Development

#### Frontend
```bash
cd client
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run linter
```

#### Backend
```bash
cd server
poetry shell         # Activate virtual environment
poetry run uvicorn app.main:app --reload  # Start dev server
poetry run pytest    # Run tests
```

#### Database
```bash
# Access Adminer
open http://localhost:8080

# Run migrations (when Alembic is set up)
cd server
poetry run alembic upgrade head
```

### Code Organization Principles

1. **Separation of Concerns**: Business logic in services, not routes
2. **Type Safety**: Use TypeScript types and Pydantic schemas
3. **Error Handling**: Consistent error responses across API
4. **Logging**: Use Loguru for all backend logging
5. **Testing**: Write tests for services, not just routes
6. **Documentation**: Keep docs/ updated with new features/patterns

### Adding New Features

1. Create feature specification in `docs/features/`
2. Implement backend service following service layer pattern
3. Create API endpoint in appropriate versioned route
4. Add frontend components/views
5. Update documentation as needed

### Adding New Patterns

1. Document pattern in `docs/patterns/`
2. Reference pattern in `CLAUDE.md` if it's a core pattern
3. Ensure all code follows the pattern
4. Update this README if pattern affects structure

## Key Design Decisions

### Why Not JWT?
- Session-based auth is simpler for server-side apps
- Easier to invalidate sessions
- Redis provides fast session storage
- No need for token refresh logic

### Why Not PostgreSQL?
- MySQL is sufficient for current needs
- Team familiarity with MySQL
- Can migrate later if needed (SQLAlchemy abstracts database)

### Why Not Pinia/Vuex?
- Vue 3 Composition API with `ref` is sufficient for current state needs
- Simpler mental model
- Can add Pinia later if state management becomes complex

### Why Not GraphQL?
- RESTful API is simpler for current requirements
- FastAPI makes REST easy and well-documented
- Can add GraphQL layer later if needed

## Future Considerations

- **State Management**: May add Pinia if state becomes complex
- **Testing**: Add E2E tests with Playwright or Cypress
- **CI/CD**: Set up GitHub Actions for automated testing
- **Monitoring**: Add application monitoring (Sentry, DataDog)
- **Caching**: Expand Redis usage beyond sessions
- **API Versioning**: Already structured for v1, v2, etc.

## References

- [CLAUDE.md](../CLAUDE.md) - Root context file with tech stack details
- [SETUP_COMMANDS.md](../SETUP_COMMANDS.md) - Detailed setup instructions
- [Features Documentation](features/) - Feature specifications
- [Patterns Documentation](patterns/) - Architectural patterns

