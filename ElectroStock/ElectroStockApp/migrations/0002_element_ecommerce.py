# Generated by Django 4.2 on 2023-04-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ElectroStockApp", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="element",
            name="ecommerce",
            field=models.BooleanField(default=0),
            preserve_default=False,
        )
    ]
