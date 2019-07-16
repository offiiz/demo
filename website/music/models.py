from django.db import models

# <Class>.objects.all() like select * from <Class>

# Create your models here.
class Album(models.Model): # like Table
    artist = models.CharField(max_length=250) # like column
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    #id will be auto-generated

    def __str__(self): #String representation of the object
        return self.album_title + " - " + self.artist 

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title