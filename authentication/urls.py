from django.urls import path

from authentication.views import UserCreateAPIView, UserLoginAPIView


app_name = 'authentication'

urlpatterns = [
    path('users/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('users/login/', UserLoginAPIView.as_view(), name="user-login"),
]