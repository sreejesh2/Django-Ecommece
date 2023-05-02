# Generated by Django 4.2 on 2023-04-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_prodictimage_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='size',
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.ManyToManyField(related_name='all_size', to='store.size'),
        ),
    ]