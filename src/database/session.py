from sqlalchemy.ext.asyncio import  async_sessionmaker, create_async_engine
from sqlalchemy.engine import URL
from src.core.config import settings

DATABASE_URL = URL.create(
    drivername = "postgresql+asyncpg",
    username = settings.DB_USER,
    password = settings.DB_PASS,
    host = settings.DB_HOST,
    port = settings.DB_PORT,
    database = settings.DB_NAME)


engine = create_async_engine(DATABASE_URL, echo = False)

AsyncSessionLocal = async_sessionmaker(bind = engine, autoflush=False, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session