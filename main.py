from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import Base, engine
from api.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan,
              title="Repository and Crypto Demo",
              redoc_url="/redoc")

app.include_router(user_router, prefix="/users")