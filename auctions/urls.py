from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories_search/<str:category>", views.categories_search, name="categories_search"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("confirmation/<str:listing_title>", views.confirmation, name="confirmation"),
    path("no_listing", views.no_listing, name="no_listing"),
    path("<str:listing_title>", views.listing_page, name="listing_page")
]
