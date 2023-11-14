from django.urls import path
from . import views

app_name = 'futebol'

urlpatterns = [
    path('teste', views.teste),
    path('estadio/list', views.list, name="estadio"),
    path('estadio/create', views.create, name="create_estadio"),
    path('estadio/update/<int:estadio_id>', views.update, name="edit_estadio"),
]