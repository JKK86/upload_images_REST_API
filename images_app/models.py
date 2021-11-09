from django.db import models
from django.utils import timezone

from upload_images_REST_API import settings


def image_directory_path(instance, filename):
    return f'images/{filename}'


class ImageUpload(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    image = models.ImageField(upload_to=image_directory_path)
    alt = models.TextField(null=True)
    uploaded = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_images')
