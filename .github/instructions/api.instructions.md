{
  "applyTo": "api/**/*.py"
}

- Use APIRouter per domain (e.g., todo_router, category_router)
- All models inherit from Base in app/models/base.py
- Use snake_case for all identifiers; PascalCase for classes
- Use SQLAlchemy 2.x async: AsyncSession, async_sessionmaker, create_async_engine
- Use aioodbc driver for SQL Server: mssql+aioodbc://
- Dependency injection: get_db() → Repository → Service → Route
- Services raise HTTPException; Repositories raise only DB exceptions
- Alembic env.py: use async engine, run_async_migrations pattern
- All tests: pytest + pytest-asyncio; use httpx.AsyncClient for API tests
- No business logic in routes or repositories
- All methods async def; always await DB calls
- Use type hints and docstrings everywhere
- Never hardcode secrets or connection strings; use environment variables
- Log exceptions with standard logging; never expose stack traces
- Validate all input with Pydantic v2 models
- Use explicit imports; avoid wildcard imports
- Keep functions short, focused, and single-responsibility
- Mock external dependencies in tests
- Never use create_all(); always use Alembic for migrations
