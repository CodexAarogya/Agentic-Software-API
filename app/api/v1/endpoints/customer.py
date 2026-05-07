from fastapi import APIRouter, Depends
from app.models.customer_model import Customer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db_connection

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings
from dotenv import load_dotenv

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


load_env = load_dotenv()

engine = create_async_engine(
    url= settings.DATABASE_URL,
    echo = True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_= AsyncSession
)

# async def get_cus():
#     return({"customer": "hello"})

@router.get("/")
async def fetch_all_customers(db: AsyncSession = Depends(get_db_connection)):
    result = await db.execute(select(Customer))
    customer = result.scalars().all()
    return({
        "Customers": [
            {
                "id": c.id
            }
            for c in customer
        ]
    })


