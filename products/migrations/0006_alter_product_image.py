# Generated by Django 3.2.25 on 2024-04-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='media/bike.bike.jpg', null=True, upload_to='products/'),
        ),
    ]
