from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Drink(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    ingredients = models.TextField()
    creationDate = models.DateTimeField(blank=True, null=True)
    
    def createDrink(self):
        self.creationDate = timezone.now
        self.save()
    
    def __str__(self):
        return self.name
    
    
class Bean(models.Model):
    country = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    creationDate = models.DateTimeField(blank=True, null=True)
    
    
    def createBean(self):
        self.creationDate = timezone.now
        self.save()
    
    def __str__(self):
        return self.name
    

