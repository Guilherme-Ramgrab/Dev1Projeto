from django.urls import path
from . import views

app_name = 'futebol'

urlpatterns = [
    path('teste', views.teste),
    path('estadio/list', views.list, name="estadio"),
]