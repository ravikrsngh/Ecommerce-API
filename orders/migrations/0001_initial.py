# Generated by Django 3.2.15 on 2022-11-08 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_receipt', models.CharField(max_length=50)),
                ('order_id', models.CharField(max_length=50)),
                ('razorpay_payment_id', models.CharField(max_length=100)),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_signature', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=100)),
                ('ship_to_name', models.CharField(max_length=100)),
                ('ship_to_phonenumber', models.CharField(max_length=15)),
                ('ship_to_street_address', models.CharField(max_length=100)),
                ('ship_to_country', models.CharField(max_length=30)),
                ('ship_to_state', models.CharField(max_length=30)),
                ('ship_to_city', models.CharField(max_length=30)),
                ('ship_to_zip', models.CharField(max_length=10)),
                ('sub_total', models.CharField(default='0', max_length=6)),
                ('tax', models.CharField(default='0', max_length=6)),
                ('cnv_charges', models.CharField(default='0', max_length=6)),
                ('discount_applied', models.CharField(default='0', max_length=6)),
                ('total', models.CharField(default='0', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
