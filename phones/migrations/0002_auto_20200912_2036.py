# Generated by Django 2.2.10 on 2020-09-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='phone', max_length=50),
        ),
    ]