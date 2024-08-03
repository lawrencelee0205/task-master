from django.db import models
from model_utils.models import UUIDModel, TimeStampedModel, SoftDeletableModel
# Create your models here.
class CommonModelMixin(UUIDModel, TimeStampedModel, SoftDeletableModel):
    class Meta:
        abstract = True