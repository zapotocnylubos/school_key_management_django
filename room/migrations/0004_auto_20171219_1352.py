# Generated by Django 2.0 on 2017-12-19 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20171219_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
