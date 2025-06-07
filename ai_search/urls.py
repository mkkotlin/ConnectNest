from django.urls import path
from ai_search.views import ai_search_view

urlpatterns = [
    path('',ai_search_view, name = 'ai_search')
]