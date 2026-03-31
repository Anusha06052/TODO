"""
Service layer for Todo business logic.
"""
from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.todo_repository import TodoRepository
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from app.db.session import get_db

class TodoService:
    """
    Provides business logic for Todo operations.
    """
    def __init__(self, repo: TodoRepository):
        """
        Initialize the service with a TodoRepository.
        """
        self.repo = repo

    async def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all Todo items.
        """
        return await self.repo.get_all()

    async def get_todo_by_id(self, todo_id: int) -> Todo:
        """
        Retrieve a Todo by its ID, raising 404 if not found.
        """
        todo = await self.repo.get_by_id(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
        return todo

    async def create_todo(self, data: TodoCreate) -> Todo:
        """
        Create a new Todo item and commit the transaction.
        """
        todo = await self.repo.create(data)
        await self.repo.db.commit()
        await self.repo.db.refresh(todo)
        return todo

    async def update_todo(self, todo_id: int, data: TodoUpdate) -> Todo:
        """
        Update an existing Todo item by ID, raising 404 if not found.
        Commits and refreshes the updated object.
        """
        todo = await self.get_todo_by_id(todo_id)
        todo = await self.repo.update(todo, data)
        await self.repo.db.commit()
        await self.repo.db.refresh(todo)
        return todo

    async def delete_todo(self, todo_id: int) -> None:
        """
        Delete a Todo item by ID, raising 404 if not found.
        Commits the transaction.
        """
        todo = await self.get_todo_by_id(todo_id)
        await self.repo.delete(todo)
        await self.repo.db.commit()

async def get_todo_service(db: AsyncSession = Depends(get_db)) -> TodoService:
    """
    FastAPI dependency to provide a TodoService instance.
    """
    return TodoService(TodoRepository(db))
