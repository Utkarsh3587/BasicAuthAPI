from django.urls import path

from crop.views import CropAPIView


app_name = 'crop'

urlpatterns = [
    path('crops/', CropAPIView.as_view(), name='crop-list'),
]