from django.db import models
from common.models import CommonModelMixin

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
