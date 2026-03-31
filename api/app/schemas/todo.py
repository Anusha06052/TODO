"""
Pydantic v2 DTOs for Todo CRUD operations.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator

class TodoBase(BaseModel):
    """
    Shared fields for Todo creation and response.
    """
    title: str = Field(..., min_length=1, max_length=200, description="Title of the todo item.")
    description: Optional[str] = Field(None, description="Optional description of the todo item.")

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Title must not be empty or whitespace.')
        return v

class TodoCreate(TodoBase):
    """
    DTO for creating a new Todo item (POST body).
    """
    pass

class TodoUpdate(BaseModel):
    """
    DTO for updating an existing Todo item (PATCH body).
    All fields are optional; only changed fields should be sent.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Title of the todo item.")
    description: Optional[str] = Field(None, description="Optional description of the todo item.")
    is_completed: Optional[bool] = Field(None, description="Completion status of the todo item.")

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError('Title must not be empty or whitespace.')
        return v

class TodoResponse(TodoBase):
    """
    DTO for returning a Todo item in API responses.
    """
    id: int = Field(..., description="Unique identifier of the todo item.")
    is_completed: bool = Field(..., description="Completion status of the todo item.")
    created_at: datetime = Field(..., description="Creation timestamp.")
    updated_at: datetime = Field(..., description="Last update timestamp.")

    model_config = ConfigDict(from_attributes=True)
