# Generated by Django 5.1.1 on 2024-10-26 10:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(choices=[('1', 'HR'), ('2', 'Engineering'), ('3', 'Sales')], null=True)),
                ('role', models.CharField(choices=[('1', 'Manager'), ('2', 'Developer'), ('3', 'Sales Representative'), ('4', 'Designer'), ('5', 'Analyst')], null=True)),
            ],
            options={
                'db_table': 'employee_master',
            },
        ),
    ]
