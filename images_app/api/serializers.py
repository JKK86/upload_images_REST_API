from rest_framework import serializers

from images_app.models import ImageUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ["id", "title", "slug", 'image', 'alt', 'uploaded', 'author']
