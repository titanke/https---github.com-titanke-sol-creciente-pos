# Generated by Django 5.0.6 on 2024-05-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0006_alter_products_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_venta',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sales',
            name='descuento',
            field=models.FloatField(default=0),
        ),
    ]
