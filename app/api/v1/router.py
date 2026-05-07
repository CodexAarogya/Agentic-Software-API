from app.api.v1.endpoints import root
from fastapi import APIRouter
router = APIRouter(
    prefix="/api/v1",
    tags=['api_version1'],
)

router.include_router(root.router)

