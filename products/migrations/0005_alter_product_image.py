# Generated by Django 3.2.25 on 2024-04-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240423_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/bike.bike.jpg', upload_to='products/'),
        ),
    ]