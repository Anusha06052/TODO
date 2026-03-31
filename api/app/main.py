"""
FastAPI application factory for the Todo API.
"""
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.routes.todo_router import router as todo_router

API_TITLE = "Todo API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Enterprise Todo application API"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_cors_origins() -> list[str]:
    origins = os.getenv("CORS_ORIGINS")
    if origins:
        return [o.strip() for o in origins.split(",") if o.strip()]
    return ["http://localhost:5173"]

def create_app() -> FastAPI:
    app = FastAPI(
        title=API_TITLE,
        version=API_VERSION,
        description=API_DESCRIPTION,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=get_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(todo_router)

    @app.get("/health", tags=["health"])
    async def health_check():
        """
        Health check endpoint. Returns API status and version.
        """
        return {"status": "ok", "version": API_VERSION}

    @app.on_event("startup")
    async def on_startup():
        logger.info("Todo API starting up")

    return app

app = create_app()
