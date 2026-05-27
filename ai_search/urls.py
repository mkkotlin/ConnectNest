from django.urls import path
from ai_search.views import ai_search_view, s_v

urlpatterns = [
    path('',ai_search_view, name = 'ai_search')
    # path('',s_v, name='s_v')
]