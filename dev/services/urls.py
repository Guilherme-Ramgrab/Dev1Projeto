from django.urls import include, path
from rest_framework import routers
from services import views

app_name = 'services'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.api_root),
    path('saudacao/', views.saudacao, name="saudacao"),
    path('estadios/', views.EstadioService.as_view(), name="estadios"),
    path('estadios/<int:pk>', views.EstadioService.as_view(), name="estadio_detail")
]

urlpatterns += router.urls