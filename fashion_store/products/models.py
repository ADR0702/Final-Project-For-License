from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    digital=models.BooleanField(default=False)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return