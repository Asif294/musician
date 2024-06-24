from django.db import models
from musicianAp.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    author = models.ForeignKey(Musician, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.album_name
