from typing import List

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from ...core.models.models import EmploymentStatus
from ...core.schemas.schemas import \
    EmploymentStatusSchema, \
    EmploymentStatusInSchema
from ..type_hints import DeletedObject


router = APIRouter(
    prefix='/employment_status',
    tags=['employment_status'])


@router.post('/', response_model=EmploymentStatusSchema)
async def create(event: EmploymentStatusInSchema):
    new_employment_status = await EmploymentStatus.create(**event.dict())
    return await EmploymentStatusSchema.from_tortoise_orm(
        new_employment_status)


@router.get('/', response_model=List[EmploymentStatusSchema])
async def list():
    return await EmploymentStatusSchema.from_queryset(EmploymentStatus.all())


@router.get('/{obj_id}', response_model=EmploymentStatusSchema)
async def retrive(obj_id: int):
    return await EmploymentStatusSchema.from_queryset_single(
        EmploymentStatus.get(id=obj_id))


@router.delete('/{obj_id}', response_model=DeletedObject)
async def delete(obj_id: int):
    try:
        await EmploymentStatus.filter(id=obj_id).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'EmploymentStatus {obj_id} not found.')

    return {'deleted': obj_id}
