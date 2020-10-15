from rest_framework import serializers

from crop.models import Crop


class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = ['id', 'title', 'created_at', 'updated_at', 'desc']
