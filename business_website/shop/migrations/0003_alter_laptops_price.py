# Generated by Django 4.1.7 on 2023-03-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_remove_laptops_quantity_laptops_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptops',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]