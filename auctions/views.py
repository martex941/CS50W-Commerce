from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, AuctionListing, Watchlist


def index(request):
    return render(request, "auctions/index.html", {
        "all_listings": AuctionListing.objects.all()
    })


def validate_url(url):
    validator = URLValidator()
    try:
        validator(url)
    except ValidationError:
        return False
    return True

@login_required
def create_listing(request):
    if request.method == "POST":
        listing_name=request.POST["title"]
        description=request.POST["description"]
        current_user=request.user
        published_by=current_user.username
        price=request.POST["bid"]
        photo=request.POST["photo"]

        # Make sure the user inputs a url to a photo and not anything else
        if validate_url(photo):
            pass
        else:
            photo = "https://img.propertyshark.com/img/no_listing_photo.png"

        category=request.POST["category"]
        new_listing=AuctionListing(name=listing_name, description=description, published_by=published_by, price=price, photo=photo, category=category)
        new_listing.save()
        return redirect("listing_page", listing_title=listing_name)

    return render(request, "auctions/create_listing.html")


def listing_page(request, listing_title):

    # Get the proper AuctionListing model
    try:
        listing_info = AuctionListing.objects.get(name=listing_title)
    except AuctionListing.DoesNotExist:
        return HttpResponseRedirect(reverse("no_listing"))
    
    user = request.user

    # Check whether the user accessing the page is the creator of the listing
    is_creator = False
    if user.username.lower() == listing_info.published_by.lower():
        is_creator = True

    all_watchlist = Watchlist.objects.all()
    new_watchlist_entry = Watchlist(watch_user=user, watch_listing=listing_info)

    # Check whether the entry exists in the watchlist
    in_watchlist = False
    if all_watchlist.filter(watch_listing=new_watchlist_entry.watch_listing):
            print(1)
            in_watchlist = True
    
    # Handle the watchlist form
    if request.method == "POST":
        if 'add-to-watchlist' in request.POST:
            new_watchlist_entry.save()
            return HttpResponseRedirect(reverse("watchlist"))
        elif 'delete-from-watchlist' in request.POST:
            delete_entry = Watchlist.objects.filter(watch_listing=new_watchlist_entry.watch_listing)
            delete_entry.delete()
            return HttpResponseRedirect(reverse("watchlist"))

    return render(request, "auctions/listing_page.html", {
        "listing": listing_info,
        "in_watchlist": in_watchlist,
        "is_creator": is_creator
    })


def no_listing(request):
    return render (request, "auctions/no_listing.html")


@login_required
def watchlist(request):
    user = request.user
    list = Watchlist.objects.filter(watch_user=user)

    return render(request, "auctions/watchlist.html", {
        "listings": list
    })


def categories(request):

    return render(request, "auctions/categories.html")


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
