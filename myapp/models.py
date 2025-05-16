from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # база с данными возвращается в отсортированном виде

    # class Meta:
    #     ordering = ['-discount']
    
    name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True, null=False)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Укорачивает описание до 48 символов
    
    # @property
    # def short_description(self):
    #     return self.descriptions if len(self.descriptions) < 48 else self.descriptions[:48], '...'
    
    
    def __str__(self):
        return f"{self.name}, {self.price}"
    
    

class Orders(models.Model):
    delivery_address = models.TextField(blank=True, null=True)
    promocode = models.CharField(max_length=50, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    
    
    def __str__(self):
        return f"{self.delivery_address}, {self.promocode}"