# Generated by Django 3.2.5 on 2021-07-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbcWinners', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
