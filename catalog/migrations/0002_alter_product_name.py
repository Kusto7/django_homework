# Generated by Django 4.2.4 on 2023-08-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, verbose_name='название продукта'),
        ),
    ]