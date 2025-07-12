from django.db import models
# Create your models here.

class AcountPost(models.Model):
    title=models.CharField(max_length=255)

