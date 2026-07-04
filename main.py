from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import health
from app.core.config import APP_DESCRIPTION, APP_NAME, APP_VERSION
from app.db.base import Base
from app.db.session import engine
from app.models import User  # noqa: F401 — register model with SQLAlchemy

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run once when the server starts, and once when it shuts down."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    lifespan=lifespan,
)

app.include_router(health.router)
