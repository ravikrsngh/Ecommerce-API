# Generated by Django 3.2.15 on 2022-11-09 03:00

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.productimage_directory_path),
        ),
    ]
