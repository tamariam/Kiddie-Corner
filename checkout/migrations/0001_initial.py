# Generated by Django 3.2.25 on 2024-05-09 14:39

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('shipping_method', models.CharField(choices=[('Standard', 'Standard Shipping'), ('Registered', 'Registered Shipping'), ('Free', 'Free Shipping')], default='standard', max_length=20)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_bag', models.TextField(default='')),
                ('order_status', models.CharField(choices=[('Received', 'Order Received'), ('Processing', 'Order Processing'), ('Dispatched', 'Order Dispatched'), ('On Hold', 'On Hold'), ('Cancelled', 'order Cancelled')], default='received', max_length=50)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
