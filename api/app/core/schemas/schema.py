from tortoise.contrib.pydantic import pydantic_model_creator

from . import models


Image = pydantic_model_creator(models.Image, name='Image')
EmploymentStatus = pydantic_model_creator(
    models.EmploymentStatus, name='EmploymentStatus')
Faculty = pydantic_model_creator(models.Faculty, name='Faculty')
User = pydantic_model_creator(models.User, name='User')
Event = pydantic_model_creator(models.Event, name='Event')
