from django.contrib import admin

from images_app.models import ImageUpload


@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ['title', 'alt', 'uploaded', 'author']
    exclude = ['uploaded']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['author', ]
    search_fields = ['title', ]

