# Generated by Django 3.2.2 on 2021-05-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
