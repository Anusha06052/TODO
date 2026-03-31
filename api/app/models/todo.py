from sqlalchemy import Integer, Boolean, DateTime, func
from sqlalchemy.dialects.mssql import NVARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Todo(Base):
    """
    ORM model for the 'todos' table.

    Represents a to-do item with title, description, completion status,
    and timestamps for creation and last update.
    """

    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Primary key, auto-incremented (SQL Server IDENTITY)"
    )
    title: Mapped[str] = mapped_column(
        NVARCHAR(200),
        nullable=False,
        comment="Short title of the todo item (max 200 chars)"
    )
    description: Mapped[str | None] = mapped_column(
        NVARCHAR(1000),
        nullable=True,
        comment="Optional detailed description (max 1000 chars)"
    )
    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="0",
        comment="Completion status (False by default)"
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        comment="Timestamp when the todo was created"
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Timestamp when the todo was last updated"
    )
