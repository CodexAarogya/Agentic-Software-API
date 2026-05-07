from fastapi import APIRouter, Depends
from app.models.customer_model import Customer
from app.schemas.customer import PaginatedCustomers
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.database.session import get_db_connection
from app.utils.paginationType import PaginationType

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/", response_model=PaginatedCustomers)
async def fetch_customers(
    pagination: PaginationType,
    db: AsyncSession = Depends(get_db_connection),
    ):

    total_results = await db.execute(select(func.count()).select_from(Customer))
    total_results = total_results.scalar()

    results = await db.execute(
        select(Customer)
        .offset(pagination.offset)
        .limit(pagination.page_size)
    )

    customers = results.scalars().all()
    print(customers)

    return PaginatedCustomers(
        total=total_results,
        page=pagination.page,
        page_size=pagination.page_size,
        data=customers
    )


