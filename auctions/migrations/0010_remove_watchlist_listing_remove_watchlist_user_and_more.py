# Generated by Django 4.2.1 on 2023-07-04 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_watchlist_listing_id_remove_watchlist_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='listing_id', to='auctions.auctionlisting'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
