from django.db import models
from common.models import CommonModelMixin

# Create your models here.
class Task(CommonModelMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey("team.Member", on_delete=models.SET_NULL, null=True, blank=True)