from django.urls import path

from crop.views import CropAPIView, CropDetailAPIView


app_name = 'crop'

urlpatterns = [
    path('crops/', CropAPIView.as_view(), name='crop-list'),
    path('crops/<int:pk>/', CropDetailAPIView.as_view(), name='crop-detail')
]