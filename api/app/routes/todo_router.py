"""
FastAPI router for Todo HTTP endpoints.
"""
from fastapi import APIRouter, Depends, Response, status
import logging
from typing import List
from app.services.todo_service import TodoService, get_todo_service
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[TodoResponse])
async def get_todos(service: TodoService = Depends(get_todo_service)):
    """
    Retrieve all todos. Returns 200 with a list of TodoResponse objects.
    """
    logger.debug("GET /todos requested")
    return await service.get_all_todos()

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(data: TodoCreate, service: TodoService = Depends(get_todo_service)):
    """
    Create a new todo. Returns 201 with the created TodoResponse.
    """
    logger.debug("POST /todos requested")
    return await service.create_todo(data)

@router.get("/{id}", response_model=TodoResponse)
async def get_todo(id: int, service: TodoService = Depends(get_todo_service)):
    """
    Retrieve a todo by ID. Returns 200 with the TodoResponse if found.
    """
    logger.debug("GET /todos/{id} requested")
    return await service.get_todo_by_id(id)

@router.patch("/{id}", response_model=TodoResponse)
async def update_todo(id: int, data: TodoUpdate, service: TodoService = Depends(get_todo_service)):
    """
    Update a todo by ID. Returns 200 with the updated TodoResponse.
    """
    logger.debug("PATCH /todos/{id} requested")
    return await service.update_todo(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(id: int, service: TodoService = Depends(get_todo_service)):
    """
    Delete a todo by ID. Returns 204 No Content on success.
    """
    logger.debug("DELETE /todos/{id} requested")
    await service.delete_todo(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
