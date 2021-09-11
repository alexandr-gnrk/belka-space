from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from ..models import models


# initialise tortoise models relationships
Tortoise.init_models(["app.core.models.models"], "models")

ImageIn = pydantic_model_creator(
    models.Image, name='ImageIn', exclude_readonly=True)
Image = pydantic_model_creator(models.Image, name='Image')

EmploymentStatus = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatusIn', exclude_readonly=True)
EmploymentStatus = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatus')

FacultyIn = pydantic_model_creator(
    models.Faculty, name='FacultyIn', exclude_readonly=True)
Faculty = pydantic_model_creator(models.Faculty, name='Faculty')

UserIn = pydantic_model_creator(
    models.User, name='UserIn', exclude_readonly=True)
User = pydantic_model_creator(models.User, name='User')

EventIn = pydantic_model_creator(
    models.Event, name='Event', exclude_readonly=True)
Event = pydantic_model_creator(models.Event, name='Event')
