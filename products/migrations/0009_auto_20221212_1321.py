# Generated by Django 3.2.15 on 2022-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_filteroptionitems_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='diamond_weight',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='gold_weight',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='gross_weight',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='making_charges',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='metal_purity',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='net_weight',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_number',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(default='', max_length=5),
        ),
    ]