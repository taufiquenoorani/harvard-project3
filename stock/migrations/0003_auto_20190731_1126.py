# Generated by Django 2.2.3 on 2019-07-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190731_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='Toppings',
            field=models.IntegerField(),
        ),
    ]
