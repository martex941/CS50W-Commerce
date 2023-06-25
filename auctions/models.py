from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
    published_by = models.CharField(max_length=64, default="N/A")
    price = models.PositiveIntegerField(default=0) 
    photo = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"
    

class Comment(models.Model):
    comment_contents = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.comment_contents}"
    

class Bid(models.Model):
    bid_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.bid_price}"