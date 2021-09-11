from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from ...core.models.models import Event
from ...core.schemas.schemas import EventSchema, EventInSchema

from ..type_hints import DeletedObject


router = APIRouter(
    prefix='/event',
    tags=['event'])


@router.post('/', response_model=EventSchema)
async def create(event: EventInSchema):
    new_event = await Event.create(**event.dict())
    return await EventSchema.from_tortoise_orm(new_event)


@router.get('/', response_model=Page[EventSchema])
async def list(params: Params = Depends()):
    return paginate(await Event.all(), params)


@router.get('/{obj_id}', response_model=EventSchema)
async def retrive(obj_id: int):
    return await EventSchema.from_queryset_single(Event.get(id=obj_id))


@router.delete('/{obj_id}', response_model=DeletedObject)
async def delete(obj_id: int):
    try:
        await Event.filter(id=obj_id).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Event {obj_id} not found.')

    return {'deleted': obj_id}
