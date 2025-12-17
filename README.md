# README.md

## Purpose of this document

Demonstrate step-by-step procedure of using ai agent from the scratch.

## Step 1. Write the root context file

- Create workspace & run claude

```sh
mkdir medi-predict-lite
cd mdedi-predict-lite
claude
```

```
/init Project: MediPredict Lite. 
Create a CLAUDE.md file.
Stack:
- Frontend: Vue 3 (Composition API), Vite, Vuetify, Chart.js, Axios (custom wrapper)
- Backend: FastAPI, SQLAlchemy, MySQL, Redis (Auth), Loguru
```

**Create symbolic links for other agents**

E.g.:
```sh
ln CLAUDE.md .cursorrules
```

## Step 2. Project Setup

- Ask AI to:
```
Act as a DevOps & System Architect.

Project: MediPredict Lite Stack:

Database: MySQL 8.0 (Docker)

Cache: Redis 7 (Docker)

Backend: FastAPI (Python 3.11, Poetry)

Frontend: Vue 3 (Vite, TypeScript, Vuetify)

Task 1: Docker Infrastructure Generate a docker-compose.yml file for the root directory.

MySQL: Expose on port 3306. Use environment variables for user/password. Create a volume for persistence.

Redis: Expose on port 6379.

Adminer: Add an Adminer container on port 8080 for easy DB management.

Task 2: Project Scaffolding Commands Provide the exact terminal commands I need to run to:

Initialize the Frontend (/client) using npm create vite@latest with Vue/TypeScript.

Install Frontend Deps: vuetify, axios, chart.js, pinia, vue-router.

Initialize the Backend (/server) using poetry init (or pip).

Install Backend Deps: fastapi, uvicorn, sqlalchemy, aiomysql (async driver), redis, loguru, pydantic-settings.

Output: Provide the docker-compose.yml content and a list of bash commands to execute.
```

- Setup development environment as instructed in `SETUP_COMMANDS.md`

**IMPORTANT**
> If there's any problem running the commands, ask AI to fix it. E.g.,
```
I found that in my environment, `docker-compose` is invalid command. Instead `docker compose` should be used. and I found the auto generated ~/.docker/config.json has typo: credsStore should be fixed to credStore. Update these to relevant documents.
```

## Step 3. Generate initial code using only the basic context

Ask AI to:
```
Create a backend endpoint to predict disease risk that uses a Python mock engine and returns a result.
```

## Step 4. Add feature and pattern docs

- Create a pattern file under docs/patterns: [**AI_INFERENCE_SERVICE.md**](__DO_NOT_READ_OR_UPDATE__/AI_INFERENCE_SERVICE.md)

- Create a feature file under docs/features: [**DISEASE_RISK_ANALYSIS.md**](__DO_NOT_READ_OR_UPDATE__/DISEASE_RISK_ANALYSIS.md)

- Add the following lines at the end of CLAUDE.md file:

```markdow
## Features & Patterns
- **Active Feature**: Disease Risk Analysis. See `docs/features/DISEASE_RISK_ANALYSIS.md` for logic and data contracts.
- **Core Pattern**: AI Service Layer. See `docs/patterns/AI_INFERENCE_SERVICE.md`. **ALL** prediction logic must follow this pattern.
```

## Step 5. Generate 'Why' document

Ask AI to:
```
Based on the project setup we just created, generate a docs/README.md that explains our folder structure, naming conventions, and tech stack choices.
```
