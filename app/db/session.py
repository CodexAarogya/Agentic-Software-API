from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings
from dotenv import load_dotenv

load_env = load_dotenv()

engine = create_async_engine(
    url= settings.DATABASE_URL,
    echo = True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_= AsyncSession
)

async def get_db_connection():
    async with SessionLocal as session:
        yield session
