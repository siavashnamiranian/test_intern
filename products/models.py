from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class store(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("owner"), on_delete=models.CASCADE)
    is_enable = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    phone_number = models.BigIntegerField()
    address = models.TextField(blank=True)

    products = models.ManyToManyField('Product', related_name='store')


class Product(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url():
        return reverse('product-detail', kwargs={'pk': self.pk})

    def clean(self):
        super().clean()
        if not "MAPSA" in self.name:
            raise ValidationError("must include mapsa")
