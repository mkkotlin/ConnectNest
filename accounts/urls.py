from django.urls import path
from accounts.views import UserRegister, logout_view, login_view


urlpatterns = [
    path('register/', UserRegister, name = 'register',),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout')
]