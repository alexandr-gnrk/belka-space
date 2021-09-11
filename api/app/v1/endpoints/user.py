from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from ...core.models.models import User
from ...core.schemas.schemas import UserSchema, UserInSchema

from ..type_hints import DeletedObject


router = APIRouter(
    prefix='/user',
    tags=['user'])


@router.post('/', response_model=UserSchema)
async def create(user: UserInSchema):
    new_user = await User.create(**user.dict())
    return await UserSchema.from_tortoise_orm(new_user)


@router.get('/', response_model=Page[UserSchema])
async def list(params: Params = Depends()):
    return paginate(
        await User.all().prefetch_related('employment_status', 'faculty'),
        params)


@router.get('/{obj_id}', response_model=UserSchema)
async def retrive(obj_id: int):
    return await UserSchema.from_queryset_single(User.get(id=obj_id))


@router.delete('/{obj_id}', response_model=DeletedObject)
async def delete(obj_id: int):
    try:
        await User.filter(id=obj_id).delete()
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {obj_id} not found.')

    return {'deleted': obj_id}
