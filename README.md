# Enterprise Todo App Monorepo

## Project Overview
A full-featured enterprise Todo application with a robust FastAPI backend and a modern React 18 frontend. Designed for scalability, maintainability, and developer productivity.

## Tech Stack
- **Backend:** FastAPI, SQLAlchemy (async), SQL Server, Alembic
- **Frontend:** React 18, TypeScript, Vite, TanStack Query, Axios

## Monorepo Structure
```
api/    # FastAPI backend
web/    # React 18 + TypeScript frontend
```

## Prerequisites
- Python 3.11+
- Node.js 18+
- SQL Server (local or remote)

## Local Setup
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd todo-app
   ```
2. **Backend setup:**
   ```sh
   cd api
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   cp .env.example .env  # Set DB connection string and secrets
   alembic upgrade head
   uvicorn app.main:app --reload
   ```
3. **Frontend setup:**
   ```sh
   cd ../web
   npm install
   cp .env.example .env  # Set VITE_API_URL
   npm run dev
   ```

## Running the App
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## Running Tests
- **Backend:**
  ```sh
  cd api
  pytest
  ```
- **Frontend:**
  ```sh
  cd web
  npm run test
  ```

## Branch Strategy
- `main`: Stable, production-ready code
- `dev`: Active development, feature integration
- `feature/*`, `fix/*`: Short-lived feature/bugfix branches

## Copilot Customization Artifacts
| Artifact                                      | Purpose/Scope                        |
|-----------------------------------------------|--------------------------------------|
| .github/copilot-instructions.md               | Workspace-wide coding standards      |
| .github/instructions/api.instructions.md      | Backend (api/) Python conventions    |
| .github/instructions/web.instructions.md      | Frontend (web/src) TypeScript rules  |
| .vscode/agents/api-agent.agent.yml            | Backend Copilot agent config         |
| .vscode/agents/web-agent.agent.yml            | Frontend Copilot agent config        |
| .github/prompts/generate-prd.prompt.md        | Product Requirements Doc generator   |
| .github/prompts/generate-trd.prompt.md        | Technical Requirements Doc generator |
| .github/prompts/commit-message.prompt.md      | Conventional commit message prompt   |
| .github/prompts/pr-review.prompt.md           | AI PR review prompt                  |
| .github/prompts/db-migration.prompt.md        | Alembic migration review prompt      |
| .github/skills/test-generator.skill.yml       | Test generation skill                |
| .github/skills/security-review.skill.yml      | Security review skill                |

## Contributing
- Follow the coding standards in `.github/copilot-instructions.md` and relevant instructions files.
- Use conventional commit messages.
- Ensure all tests pass before submitting a PR.
- Open issues or discussions for major changes.
