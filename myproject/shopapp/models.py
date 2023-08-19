from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'
        ordering = ['name', 'price']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Product {self.pk},   {self.name}'

    # @property
    # def description_short(self):
    #     if len(self.description) < 48:
    #         return self.description
    #     return self.description[:48] + '...'


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")

# Create your models here.
    class Meta:
        db_table = 'orders'
        # ordering = ['name', 'price']
        # verbose_name = 'product'
        # verbose_name_plural = 'products'

    def __str__(self):
        return f'Order {self.pk}, address - {self.delivery_address}'
