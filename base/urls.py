from django.contrib import admin
from django.urls import path
from .views import WishPage, Home

urlpatterns = [
    path('display/', WishPage.as_view(), name='wishpage'),
    path('home/', Home.as_view(), name='home'),
]