from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return '{}'.format(self.name)