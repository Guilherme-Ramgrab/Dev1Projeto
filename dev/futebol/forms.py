from django.forms import ModelForm
from futebol.models.estadio import Estadio

class EstadioForm(ModelForm):
    class Meta:
        model = Estadio
        fields = '__all__'