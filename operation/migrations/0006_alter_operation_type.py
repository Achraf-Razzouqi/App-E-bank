# Generated by Django 3.2.2 on 2021-05-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20210528_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]