# Generated by Django 3.1 on 2020-08-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='products',
            field=models.ManyToManyField(related_name='store', to='products.Product'),
        ),
    ]