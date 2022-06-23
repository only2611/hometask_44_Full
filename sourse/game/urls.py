from django.contrib import admin
from django.urls import path

from game.views import index_view, history_stat

urlpatterns = [
    path("", index_view),
    path('history/', history_stat)
]