import os
import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings for loading DATABASE_URL from environment or .env
class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATABASE_URL: str | None = None

settings = DBSettings()
logger = logging.getLogger("db.session")

if not settings.DATABASE_URL:
    logger.warning("DATABASE_URL environment variable is not set. Database connections will fail.")

engine = create_async_engine(
    settings.DATABASE_URL or "",
    echo=False,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides a SQLAlchemy AsyncSession.

    Yields:
        AsyncSession: An active async database session.

    Usage:
        async def endpoint(db: AsyncSession = Depends(get_db)):
            ...
    """
    session: AsyncSession = AsyncSessionLocal()
    try:
        yield session
    finally:
        await session.close()
