# Generated by Django 4.2.1 on 2023-07-04 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_watchlist_listing_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user_id',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.auctionlisting'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
