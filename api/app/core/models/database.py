from tortoise import models, fields


# CharField max length
MAX_LENGTH = 255


class Image(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(MAX_LENGTH)
    url = fields.CharField(MAX_LENGTH)


class EmploymentStatus(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(MAX_LENGTH)


class Faculty(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(MAX_LENGTH)
    abbreviation = fields.CharField(MAX_LENGTH)


class User(models.Model):

    id = fields.IntField(pk=True)
    first_name = fields.CharField(MAX_LENGTH)
    second_name = fields.CharField(MAX_LENGTH)
    email = fields.CharField(MAX_LENGTH, unique=True)
    telegram_id = fields.CharField(MAX_LENGTH, unique=True)
    telegram_username = fields.CharField(MAX_LENGTH, unique=True)
    studing_at_kpi = fields.BooleanField()
    graduated_from_kpi = fields.BooleanField()
    kpi_admission_year = fields.DatetimeField()
    faculty = fields.ForeignKeyField(
        'models.Faculty', related_name='graduates')
    employment_status = fields.ForeignKeyField(
        'models.EmploymentStatus', related_name='users')


class Event(models.Model):

    id = fields.IntField(pk=True)
    title = fields.CharField(MAX_LENGTH)
    description = fields.TextField()
    start_time = fields.DatetimeField()
    image = fields.OneToOneField('models.Image', related_name='event')
    visitors = fields.ManyToManyField('models.User', related_name='events') 
