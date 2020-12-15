from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='static/user_images', null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        if not self.phone:
            raise ValueError("telephone ro vared kon")
        if not self.username:
            user = User.objects.create(username=self.phone)
            self.username = user
        return super().save(*args, **kwargs)


class Supplier(models.Model):
    store_name = models.CharField(max_length=25, default=" ")
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name


class Address(models.Model):
    STATE = [
        ('tehran', 'تهران'),
        ('khouzestan', 'خوزستان'),
        ('ardebil', 'اردبیل')
    ]
    state = models.CharField(max_length=20, choices=STATE, verbose_name="استان")
    city = models.CharField(max_length=20, verbose_name="شهر")
    street = models.CharField(max_length=20, verbose_name="خیابان")
    alley = models.CharField(max_length=20, verbose_name="کوچه")
    plate = models.IntegerField(verbose_name="پلاک")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    priority = models.SmallIntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
