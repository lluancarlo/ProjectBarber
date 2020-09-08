import uuid

from django.db import models
from django.utils.http import int_to_base36

LENGTH_OF_ID = 12


def generate_id() -> str:
    """Generates random string with length of `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:LENGTH_OF_ID]


# Create your models here.


class User(models.Model):
    id = models.CharField(
        max_length=LENGTH_OF_ID, primary_key=True, default=generate_id, editable=False
    )
    name = models.CharField(max_length=255)
    admin = models.BooleanField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
