from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from ..models import models


# initialise tortoise models relationships
Tortoise.init_models(["app.core.models.models"], "models")

ImageInSchema = pydantic_model_creator(
    models.Image, name='ImageIn', exclude_readonly=True)
ImageSchema = pydantic_model_creator(
    models.Image, name='Image', exclude=['event'])

EmploymentStatusInSchema = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatusIn', exclude_readonly=True)
EmploymentStatusSchema = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatus')

FacultyInSchema = pydantic_model_creator(
    models.Faculty, name='FacultyIn', exclude_readonly=True)
FacultySchema = pydantic_model_creator(models.Faculty, name='Faculty')

UserInSchema = pydantic_model_creator(
    models.User, name='UserIn', exclude_readonly=True)
UserSchema = pydantic_model_creator(models.User, name='User')

EventInSchema = pydantic_model_creator(
    models.Event, name='Event', exclude_readonly=True)
EventSchema = pydantic_model_creator(models.Event, name='Event')
