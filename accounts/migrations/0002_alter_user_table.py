# Generated by Django 5.0.7 on 2024-08-25 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='custom_user',
        ),
    ]
