# Generated by Django 5.1.1 on 2024-10-12 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establisment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField()),
                ('category', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('establisment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='establisment.establisment')),
            ],
        ),
    ]
