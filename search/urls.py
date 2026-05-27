from django.urls import path
from search.views import search, filter_s, notifications_api

urlpatterns = [
    path('search/', search, name='search'),
    path('filter_s/', filter_s, name='filter_s'),
    path('notifications/', notifications_api, name='notifications_api'),
]