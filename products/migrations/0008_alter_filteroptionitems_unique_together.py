# Generated by Django 3.2.15 on 2022-11-28 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_filteroptionitems_icon'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='filteroptionitems',
            unique_together={('name', 'filter')},
        ),
    ]
