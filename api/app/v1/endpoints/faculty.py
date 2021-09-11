from typing import List

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from ...core.models.models import Faculty
from ...core.schemas.schemas import FacultySchema, FacultyInSchema
from ..type_hints import DeletedObject


router = APIRouter(
    prefix='/faculty',
    tags=['faculty'])


@router.post('/', response_model=FacultySchema)
async def create(event: FacultyInSchema):
    new_faculty = await Faculty.create(**event.dict())
    return await FacultySchema.from_tortoise_orm(new_faculty)


@router.get('/', response_model=List[FacultySchema])
async def list():
    return await FacultySchema.from_queryset(Faculty.all())


@router.get('/{obj_id}', response_model=FacultySchema)
async def retrive(obj_id: int):
    return await FacultySchema.from_queryset_single(Faculty.get(id=obj_id))


@router.delete('/{obj_id}', response_model=DeletedObject)
async def delete(obj_id: int):
    try:
        await Faculty.filter(id=obj_id).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Faculty {obj_id} not found.')

    return {'deleted': obj_id}
