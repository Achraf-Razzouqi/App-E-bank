# Generated by Django 3.2.2 on 2021-05-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_use_cheque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='use',
            name='cheque',
            field=models.CharField(default='non', max_length=50, null=True),
        ),
    ]
