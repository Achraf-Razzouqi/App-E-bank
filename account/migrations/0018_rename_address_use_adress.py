# Generated by Django 3.2.2 on 2021-05-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210528_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='use',
            old_name='address',
            new_name='adress',
        ),
    ]