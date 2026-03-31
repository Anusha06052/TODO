from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Declarative base class for all ORM models.

    All SQLAlchemy models in this application should inherit from this Base
    to share metadata and configuration.
    """
    pass
