# Generated by Django 3.2.16 on 2023-02-17 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_cartitems_cartitem'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
