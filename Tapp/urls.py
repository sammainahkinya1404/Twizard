# from django import views
from django.urls import path

from Tapp import views


urlpatterns = [
    path('',views.index,name="index"),
   
   
    
]


