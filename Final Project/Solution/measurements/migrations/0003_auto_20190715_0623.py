# Generated by Django 2.0.13 on 2019-07-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20190715_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
