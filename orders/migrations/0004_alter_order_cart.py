# Generated by Django 3.2.16 on 2023-02-17 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_cartitems_cartitem'),
        ('orders', '0003_auto_20230217_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cart.cart'),
        ),
    ]
