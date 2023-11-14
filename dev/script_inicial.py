from futebol.models.estadio import Estadio
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs2023')
