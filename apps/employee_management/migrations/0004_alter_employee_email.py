# Generated by Django 5.1.1 on 2024-10-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0003_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
