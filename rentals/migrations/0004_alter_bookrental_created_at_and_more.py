# Generated by Django 4.0.5 on 2022-06-02 18:20

from django.db import migrations, models
import rentals.models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_alter_bookrental_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrental',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookrental',
            name='return_date',
            field=models.DateTimeField(default=rentals.models.calculate_return_date),
        ),
    ]
