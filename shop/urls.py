from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
path('', views.index, name="Home"),

path('about/', views.about, name="About"),

path('contact/', views.contact, name="Contact"),

path('login/', views.login, name="Login"),

path('time/',  views.time, name ="Time"),

path('coaching/',  views.coach, name ="coach")



]