# Generated by Django 5.0.6 on 2024-05-18 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
