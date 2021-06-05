# Generated by Django 3.2.2 on 2021-05-29 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_reclamation'),
        ('operation', '0008_auto_20210529_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='idD',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='idD', to='account.use'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='idR',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='idR', to='account.use'),
        ),
    ]
