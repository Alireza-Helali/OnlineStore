from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from userprofile.models import Profile


class ShopCart(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    payment_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username


class ShopCartItem(models.Model):
    count = models.IntegerField()
    shop_cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.id} - {self.product.name}"

