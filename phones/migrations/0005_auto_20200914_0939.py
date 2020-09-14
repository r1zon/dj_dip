# Generated by Django 2.2.10 on 2020-09-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='product',
        ),
        migrations.AddField(
            model_name='article',
            name='products',
            field=models.ManyToManyField(related_name='articles', to='phones.Product'),
        ),
    ]