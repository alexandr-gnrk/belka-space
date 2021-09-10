from fastapi import APIRouter

from ...core.models import models
from ...core.schemas import schemas


router = APIRouter(
    prefix='/image',
    tags=['image'])


@router.post('/', response_model=schemas.Image)
async def create_image(image: schemas.Image):
    print(schema.Image)
    return 'Hello, this is a snippet.'
