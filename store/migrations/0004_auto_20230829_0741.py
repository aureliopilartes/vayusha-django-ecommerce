# Generated by Django 3.1.7 on 2023-08-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
