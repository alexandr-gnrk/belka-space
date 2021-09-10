from fastapi import APIRouter

from .endpoints import image


router = APIRouter(
    prefix='/api/v1',
    tags=['v1'])

router.include_router(image.router)
