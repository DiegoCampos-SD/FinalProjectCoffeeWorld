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

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    drink = models.ForeignKey(Drink, null=True, blank=True, on_delete=models.SET_NULL) 
    bean = models.ForeignKey(Bean, null=True, blank=True, on_delete=models.SET_NULL) 
    quantity = models.IntegerField()
    total_price = models.FloatField(blank=True, null=True)  
    order_date = models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=20, default='pending') 

    def save(self, *args, **kwargs):
        # Automatically calculate the total price based on the quantity
        if self.drink:
            self.total_price = self.drink.price * self.quantity
        elif self.bean:
            self.total_price = self.bean.price * self.quantity
        super().save(*args, **kwargs)

<<<<<<< HEAD
    def __str__(self):
        return f"Order by {self.user} on {self.order_date}"

=======
    def str(self):
        return f"Order by {self.user} on {self.order_date}"
>>>>>>> a8a292c8fad98893eda100796cfdd561659c9c79
