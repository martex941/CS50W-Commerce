# Generated by Django 4.2.1 on 2023-06-26 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
