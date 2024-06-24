from django.shortcuts import render,redirect
from . import forms
from . models import Album
def album(request):
    if request.method=="POST":
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form=forms.AlbumForm()
    return render(request,'album.html',{'form':album_form})


def edit_album(request,id):
    albums=Album.objects.get(pk=id) 
    album_form=forms.AlbumForm(instance=albums)
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST, instance=albums)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    
    return render(request,'album.html',{'form':album_form})

def delete_album(request,id):
    albums=Album.objects.get(pk=id) 
    albums.delete()
    return redirect("homepage")
