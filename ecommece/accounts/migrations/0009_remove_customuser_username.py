# Generated by Django 4.2 on 2023-04-18 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
