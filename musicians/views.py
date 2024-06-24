from django.shortcuts import render
from album.models import Album
def home(request):
    data = Album.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)