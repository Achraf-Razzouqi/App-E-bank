# Generated by Django 3.2.2 on 2021-05-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_auto_20210531_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamation',
            name='Adate',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
