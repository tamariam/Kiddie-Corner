# Generated by Django 3.2.25 on 2024-06-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_alter_testimonial_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials/'),
        ),
    ]
