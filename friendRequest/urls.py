from django.urls import path
from friendRequest.views import acceptRequest, rejectRequest, sendFrq

urlpatterns = [
    path('send/<str:username>/', sendFrq, name='send request'),
    path('accept/<int:request_id>/', acceptRequest, name = 'accept request'),
    path('reject/<int:request_id>/', rejectRequest, name = 'reject request')
]