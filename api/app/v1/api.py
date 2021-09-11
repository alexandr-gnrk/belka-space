from fastapi import APIRouter

from .endpoints import image, event


router = APIRouter(
    prefix='/api/v1',
    tags=['v1'])

router.include_router(image.router)
router.include_router(event.router)
