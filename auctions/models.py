from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
    published_by = models.CharField(max_length=64, default="N/A")
    price = models.PositiveIntegerField(default=0) 
    photo = models.CharField(max_length=250)
    category = models.CharField(max_length=64, default="")
    date_created=models.DateTimeField(default=timezone.now, editable=False)
    is_closed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, published by {self.published_by}"
    

class Comment(models.Model):
    comment_contents = models.CharField(max_length=250)
    comment_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comment_listing", default="")
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", default="")
    comment_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.comment_contents}"
    

class Bid(models.Model):
    bid_price = models.PositiveIntegerField(default=0)
    bid_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bid_listing", default="")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user", default="")
    bid_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.bid_price} by {self.bid_user} on {self.bid_listing}"
    
class Watchlist(models.Model):
    watch_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="watch_listing", default="")
    watch_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch_user", default="")

    def __str__(self):
        return f"{self.watch_listing}, watched by {self.watch_user}"