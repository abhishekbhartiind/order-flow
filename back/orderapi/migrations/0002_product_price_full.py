# Generated by Django 3.2.19 on 2023-08-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_full',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
