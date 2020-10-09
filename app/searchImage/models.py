from django.db import models

# Create your models here.
class Query(models.Model):
    id = models.CharField(primary_key = True, max_length = 50)
    img = models.ImageField(upload_to = "img")
    status = models.CharField(max_length = 50)
    result = models.CharField(blank = True, null = True, max_length = 200)
    individualRes = models.CharField(blank = True, null = True, max_length = 200)
    submitTime = models.DateTimeField(blank = True, null = True)
    recognizeTime = models.DateTimeField(blank = True, null = True)
