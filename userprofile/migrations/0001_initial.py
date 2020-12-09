# Generated by Django 3.1.4 on 2020-12-07 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/user_images')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(default=' ', max_length=25)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('tehran', 'تهران'), ('khouzestan', 'خوزستان'), ('ardebil', 'اردبیل')], max_length=20, verbose_name='استان')),
                ('city', models.CharField(max_length=20, verbose_name='شهر')),
                ('street', models.CharField(max_length=20, verbose_name='خیابان')),
                ('alley', models.CharField(max_length=20, verbose_name='کوچه')),
                ('plate', models.IntegerField(verbose_name='پلاک')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('priority', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.profile')),
            ],
        ),
    ]
