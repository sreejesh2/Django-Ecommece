# Generated by Django 4.2 on 2023-05-06 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_productgender_product_and_more'),
        ('cart', '0005_remove_cart_price_cart_productsizeprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='productSizePrice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productsizeprice'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productcolor'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price', to='store.productprice'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productsize'),
        ),
    ]
