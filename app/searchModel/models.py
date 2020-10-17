from django.db import models

# Create your models here.
class QueryThree(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    subId = models.IntegerField()
    status = models.CharField(max_length=50)
    requestTime = models.DateTimeField(blank=True, null=True)
    reconstructionTime = models.DateTimeField(blank=True, null=True)
