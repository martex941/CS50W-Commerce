# Generated by Django 4.2.3 on 2023-07-10 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_bid_bid_date_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_listing',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment_listing', to='auctions.auctionlisting'),
        ),
    ]
