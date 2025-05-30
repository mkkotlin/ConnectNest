from django.urls import path
from search.views import search, filter_s

urlpatterns = [
    path('search/', search, name = 'search'),
    path('filter_s/', filter_s, name = 'filter_s'),
]