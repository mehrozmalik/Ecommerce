# Generated by Django 3.1.7 on 2021-06-09 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeliveryOption',
            new_name='DeliveryOptions',
        ),
    ]