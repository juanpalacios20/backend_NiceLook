# Generated by Django 5.0.6 on 2024-10-01 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('schedule', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('estate', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule')),
                ('services', models.ManyToManyField(to='service.service')),
            ],
        ),
    ]