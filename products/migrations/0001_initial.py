# Generated by Django 3.2.15 on 2022-10-06 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('lvl1', 'Level 1'), ('lvl2', 'Level 2'), ('lvl3', 'Level 3'), ('lvl4', 'Level 4')], default='lvl1', max_length=10)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]