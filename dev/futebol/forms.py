from django.forms import ModelForm
from futebol.models.estadio import Estadio

class EstadioForm(ModelForm):
    class Meta:
        model = Estadio
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(EstadioForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})