# Generated by Django 5.1.1 on 2024-10-08 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('establisment', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField()),
                ('total', models.FloatField()),
                ('discount', models.FloatField(null=True)),
                ('date', models.DateField()),
                ('method', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('establisment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establisment.establisment')),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]
