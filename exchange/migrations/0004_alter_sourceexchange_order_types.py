# Generated by Django 4.1.2 on 2022-11-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_tradetype_remove_sourceexchange_order_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceexchange',
            name='order_types',
            field=models.ManyToManyField(blank=True, to='exchange.tradetype'),
        ),
    ]
