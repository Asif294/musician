from django.shortcuts import render,redirect
from django.contrib import messages
from .import forms ,models
from django.contrib.auth.forms import UserCreationForm
from album.models import Album
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import MusicianForm
from django.contrib.auth.models import User
class SignUpView( CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('user_login')
  form_class = UserCreationForm
 

class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'profile'
        return context
    


def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def profile(request):
    data = Album.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

def add_musician(request):
    if request.method=="POST":
        MusicianForm=forms.MusicianForm(request.POST)
        if MusicianForm.is_valid():
            MusicianForm.save()
            return redirect("homepage")
    else:
        MusicianForm=forms.MusicianForm()
    return render(request,'musician.html',{'form':MusicianForm})

def edit_musician(request,id):
    music=models.Musician.objects.get(pk=id) 
    MusicianForm=forms.MusicianForm(instance=music)
    if request.method=='POST':
        MusicianForm=forms.MusicianForm(request.POST, instance=music)
        if MusicianForm.is_valid():
            MusicianForm.save()
            return redirect("homepage")
    return render(request,'musician.html',{'form':MusicianForm})