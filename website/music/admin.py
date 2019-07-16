from django.contrib import admin
from music.models import Album, Song

# Register your models here.
# It means add your model to Django admin GUI page
admin.site.register(Album)
admin.site.register(Song)

