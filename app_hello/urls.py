from django.contrib import admin
from django.urls import path, include
from .views import go_display_hello

urlpatterns = [
    path('test/', go_display_hello),
]
