
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.groups, name = 'groups'),
    path('techxanime/', views.techxanime, name = 'techxanime'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('anime', views.anime, name = 'anime'),
    path('register/', views.registerPage, name='register' ),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('create_/<str:pk>/', views.createSpecialization, name='create'),
    path('update_s/<str:pk>/', views.updateSpecialization, name='update_s'),
    path('delete_s/<str:pk>/', views.deleteSpecialization, name='delete_s'),
    path('user/', views.userPage, name = 'user_page'),



]