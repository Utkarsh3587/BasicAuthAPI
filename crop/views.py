from rest_framework import generics
from rest_framework.response import Response

from crop.serializers import CropSerializer
from crop.models import Crop


class CropAPIView(generics.ListCreateAPIView):
    serializer_class = CropSerializer


    def get(self, request, *args, **kwargs):
        crops = Crop.objects.all()[:10]
    
        return Response(CropSerializer(crops, many=True).data)