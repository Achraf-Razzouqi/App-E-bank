# Generated by Django 3.2.2 on 2021-05-11 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
    ]