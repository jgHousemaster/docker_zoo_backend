from django.db import models

# Create your models here.


class AnimalInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
