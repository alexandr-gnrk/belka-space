from fastapi import APIRouter

from .endpoints import \
    image, event, user, faculty, employment_status


router = APIRouter(
    prefix='/api/v1',
    tags=['v1'])

router.include_router(image.router)
router.include_router(event.router)
router.include_router(user.router)
router.include_router(faculty.router)
router.include_router(employment_status.router)
