from django.contrib import admin
from django.urls import path,include
from mainApp import views

urlpatterns = [
    path('', views.blogpost, name='home'),
    path('<str:slug>',views.bloghome,name = 'bloghome')
]
