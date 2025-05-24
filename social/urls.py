from django.urls import path
from social.views import dashboard_view


urlpatterns = [path("dashboard/", dashboard_view, name="dashboard")]
