from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, AuctionListing, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "all_listings": AuctionListing.objects.all()
    })


@login_required
def create_listing(request):
    if request.method == "POST":
        listing_name=request.POST["title"]
        description=request.POST["description"]
        current_user=request.user
        published_by=current_user.username
        price=request.POST["bid"]
        photo=request.POST["photo"]
        category=request.POST["category"]
        new_listing=AuctionListing(name=listing_name, description=description, published_by=published_by, price=price, photo=photo, category=category)
        new_listing.save()
        return HttpResponseRedirect(reverse(f"{listing_name}"))

    return render(request, "auctions/create_listing.html")


def listing_page(request, listing_title):
    try:
        listing_info = AuctionListing.objects.get(name=listing_title)
    except AuctionListing.DoesNotExist:
        return HttpResponseRedirect(reverse("no_listing"))
    
    return render(request, "auctions/listing_page.html", {
        "listing": listing_info
    })


def no_listing(request):
    return render (request, "auctions/no_listing.html")


@login_required
def watchlist(request):
    user_id = request.user.id
    listings = AuctionListing.objects.all()
    print(listings)
    watchlist_items = listings.filter(id__in=listings)
    print(watchlist_items)
    list = Watchlist.objects.all()
    print(list)

    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
