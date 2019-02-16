from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('home/delete', views.delete)

]
