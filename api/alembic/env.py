
# Async Alembic env.py for SQL Server (MSSQL)
import asyncio
import os
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context

# Load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import Base and all models so metadata is populated
from app.models.base import Base
import app.models.todo  # side-effect import for metadata

target_metadata = Base.metadata

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=False,  # Not needed for SQL Server
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    """
    Run migrations in 'online' mode using AsyncEngine.
    """
    connectable = create_async_engine(DATABASE_URL, pool_pre_ping=True)
    async with connectable.begin() as conn:
        await conn.run_sync(
            lambda sync_conn: context.configure(
                connection=sync_conn,
                target_metadata=target_metadata,
                render_as_batch=False,  # Not needed for SQL Server
            )
        )
        await conn.run_sync(context.run_migrations)
    await connectable.dispose()

def run_migrations_online() -> None:
    """
    Entrypoint for running async migrations in sync context.
    """
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
