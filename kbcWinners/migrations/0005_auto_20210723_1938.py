# Generated by Django 3.2.5 on 2021-07-23 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kbcWinners', '0004_auto_20210723_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 19, 38, 41, 511572, tzinfo=utc), verbose_name='date published'),
        ),
    ]