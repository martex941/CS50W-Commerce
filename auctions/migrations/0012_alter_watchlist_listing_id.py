# Generated by Django 4.2.1 on 2023-07-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_watchlist_listing_id_alter_watchlist_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listing_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_id', to='auctions.auctionlisting'),
        ),
    ]
