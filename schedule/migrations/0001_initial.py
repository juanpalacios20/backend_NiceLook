# Generated by Django 5.1.1 on 2024-11-13 19:13

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('establisment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('establisment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establisment.establisment')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start_day_one', models.TimeField()),
                ('time_end_day_one', models.TimeField()),
                ('time_start_day_two', models.TimeField(null=True)),
                ('time_end_day_two', models.TimeField(null=True)),
                ('double_day', models.BooleanField()),
                ('state', models.BooleanField()),
                ('working_days', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
