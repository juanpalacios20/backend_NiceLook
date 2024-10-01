# Generated by Django 5.1.1 on 2024-09-30 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
        ('establisment', '0003_alter_establisment_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='establisment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='establisment.establisment'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
