# Setup Commands for MediPredict Lite Stack

## Docker Infrastructure Setup

1. **Start Docker services:**
```bash
docker-compose up -d
```

2. **Check service status:**
```bash
docker-compose ps
```

3. **View logs:**
```bash
docker-compose logs -f
```

4. **Stop services:**
```bash
docker-compose down
```

5. **Stop and remove volumes (clean slate):**
```bash
docker-compose down -v
```

## Frontend Setup (/client)

1. **Initialize Vue 3 project with Vite and TypeScript:**
```bash
npm create vite@latest client -- --template vue-ts
```

2. **Navigate to client directory:**
```bash
cd client
```

3. **Install base dependencies:**
```bash
npm install
```

4. **Install additional frontend dependencies:**
```bash
npm install vuetify axios chart.js pinia vue-router
```

5. **Install Vuetify dependencies:**
```bash
npm install @mdi/font
```

6. **Return to root directory:**
```bash
cd ..
```

## Backend Setup (/server)

### Option 1: Using Poetry (Recommended)

1. **Install Poetry (if not already installed):**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Create server directory and initialize Poetry:**
```bash
mkdir -p server
cd server
poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python "^3.11"
```

3. **Add backend dependencies:**
```bash
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

4. **Install dependencies:**
```bash
poetry install
```

5. **Return to root directory:**
```bash
cd ..
```

### Option 2: Using pip and venv

1. **Create server directory and virtual environment:**
```bash
mkdir -p server
cd server
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Upgrade pip:**
```bash
pip install --upgrade pip
```

3. **Install backend dependencies:**
```bash
pip install fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

4. **Create requirements.txt:**
```bash
pip freeze > requirements.txt
```

5. **Return to root directory:**
```bash
cd ..
```

## Quick Start (All-in-One)

Run these commands in sequence from the project root:

```bash
# 1. Start Docker services
docker-compose up -d

# 2. Setup Frontend
npm create vite@latest client -- --template vue-ts
cd client
npm install
npm install vuetify axios chart.js pinia vue-router @mdi/font
cd ..

# 3. Setup Backend (Poetry)
mkdir -p server
cd server
poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python "^3.11"
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
poetry install
cd ..
```

## Access Points

- **MySQL**: `localhost:3306`
- **Redis**: `localhost:6379`
- **Adminer**: `http://localhost:8080`
  - System: MySQL
  - Server: mysql
  - Username: mediuser (or root)
  - Password: medipassword (or rootpassword)
  - Database: medipredict

