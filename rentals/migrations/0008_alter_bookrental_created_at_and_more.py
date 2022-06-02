# Generated by Django 4.0.5 on 2022-06-02 18:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import rentals.models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_alter_bookrental_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrental',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 18, 27, 17, 691019, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bookrental',
            name='return_date',
            field=models.DateTimeField(default=rentals.models.calculate_return_date),
        ),
    ]