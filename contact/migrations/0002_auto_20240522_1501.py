# Generated by Django 3.2.25 on 2024-05-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='pending',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=20),
        ),
    ]
