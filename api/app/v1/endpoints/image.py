from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

from ...core.models.models import Image
from ...core.schemas.schemas import ImageSchema, ImageInSchema
from ..type_hints import DeletedObject


router = APIRouter(
    prefix='/image',
    tags=['image'])


@router.post('/', response_model=ImageSchema)
async def create(image: ImageInSchema):
    new_image = await Image.create(**image.dict())
    return await ImageSchema.from_tortoise_orm(new_image)


@router.get('/{obj_id}', response_model=ImageSchema)
async def retrive(obj_id: int):
    return await ImageSchema.from_queryset_single(Image.get(id=obj_id))


@router.delete('/{obj_id}', response_model=DeletedObject)
async def delete(obj_id: int):
    try:
        await Image.filter(id=obj_id).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Image {obj_id} not found.')

    return {'deleted': obj_id}
