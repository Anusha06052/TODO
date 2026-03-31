"""
Async SQLAlchemy repository for Todo data access.
"""
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update as sa_update, delete as sa_delete
from sqlalchemy.orm import selectinload
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

class TodoRepository:
    """
    Repository for performing CRUD operations on Todo objects.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the repository with an AsyncSession.
        """
        self.db = db

    async def get_all(self) -> List[Todo]:
        """
        Retrieve all Todo items, ordered by created_at descending.
        """
        stmt = select(Todo).order_by(Todo.created_at.desc())
        result = await self.db.scalars(stmt)
        return list(result)

    async def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a Todo item by its ID.
        Returns None if not found.
        """
        stmt = select(Todo).where(Todo.id == todo_id)
        result = await self.db.scalar_one_or_none(stmt)
        return result

    async def create(self, todo: TodoCreate) -> Todo:
        """
        Create a new Todo item from a TodoCreate schema.
        """
        db_todo = Todo(**todo.model_dump())
        self.db.add(db_todo)
        # Do not commit here; handled by service layer
        await self.db.flush()
        return db_todo

    async def update(self, todo: Todo, data: TodoUpdate) -> Todo:
        """
        Update an existing Todo item with fields from TodoUpdate.
        Only fields present in model_fields_set are updated.
        """
        # model_fields_set contains only the fields explicitly set by the client
        for field in data.model_fields_set:
            value = getattr(data, field)
            setattr(todo, field, value)
        # Do not commit here; handled by service layer
        await self.db.flush()
        return todo

    async def delete(self, todo: Todo) -> None:
        """
        Delete a Todo item from the database.
        """
        await self.db.delete(todo)
        # Do not commit here; handled by service layer
        await self.db.flush()
