from django.db import models
from userprofile.models import Supplier
import os


def upload_image_path(instance, file_path):
    name, ext = os.path.splitext(file_path)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return final_name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    image = models.ImageField(upload_to=f'static/images')
    quantity = models.IntegerField(default=0)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{self.pk}/{self.name.replace(' ', '-')}"


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.product.name


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=15)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.title
