from django.db import models


class Crop(models.Model):
    title = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    descripttion = models.TextField(default='Crop Details')

    def __str__(self):
        return self.title