from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
   path('',views.index),
   path('create/',views.registration),
   path('login/',views.login),
   path('user_login/',views.user_login),
   path('welcome/',views.welcome),
   path('data/',views.data),
   path('deletedata/',views.deletedata),
   path('update_data/',views.update_data),
   path('update/',views.update)
 
  
]
