from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

from ...core.models.models import Image
from ...core.schemas.schemas import ImageSchema, ImageInSchema


router = APIRouter(
    prefix='/image',
    tags=['image'])


@router.post('/', response_model=ImageSchema)
async def create(image: ImageInSchema):
    new_image = await Image.create(**image.dict())
    return await ImageSchema.from_tortoise_orm(new_image)


@router.get('/{id_}', response_model=ImageSchema)
async def retrive(id_: int):
    return await ImageSchema.from_queryset_single(Image.get(id=id_))


@router.delete('/{id_}', response_model=dict)
async def delete(id_: int):
    try:
        await Image.filter(id=id_).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Image {id_} not found.')

    return {'deleted': id_}
