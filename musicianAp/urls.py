from django.urls import path,include
from . import views

urlpatterns = [
    path("register/", views.SignUpView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('',views.add_musician,name='musician'),
    path('edit_mu/<int:id>',views.edit_musician,name='edit_musician')
    
]