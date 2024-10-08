import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    activation_key = models.UUIDField(default=uuid.uuid4)