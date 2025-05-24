from django.urls import path
from social.views import dashboard_view, update_bio


urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path('update_bio/', update_bio, name = 'update_bio')
]
