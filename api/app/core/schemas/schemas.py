from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from ..models import models


# initialise tortoise models relationships
Tortoise.init_models(["app.core.models.models"], "models")

ImageIn = pydantic_model_creator(models.Image, name='ImageIn', exclude='id')
Image = pydantic_model_creator(models.Image, name='Image')

EmploymentStatus = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatusIn', exclude='id')
EmploymentStatus = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatus')

FacultyIn = pydantic_model_creator(
    models.Faculty, name='FacultyIn', exclude='id')
Faculty = pydantic_model_creator(models.Faculty, name='Faculty')

UserIn = pydantic_model_creator(models.User, name='UserIn', exclude='id')
User = pydantic_model_creator(models.User, name='User')

EventIn = pydantic_model_creator(models.Event, name='Event', exclude='id')
Event = pydantic_model_creator(models.Event, name='Event')
