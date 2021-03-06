# Generated by Django 3.2.9 on 2021-11-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingridients',
        ),
        migrations.AlterField(
            model_name='clients',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='mixtures',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
