from .base import BaseModel
from django.db import models
import datetime
from django.core.validators import MinLengthValidator
import random, string


class Estadio(BaseModel):
    nome = models.CharField(max_length=200,
                            verbose_name="Nome",
                            help_text="Digite o nome do estádio")
    cod = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11)],
                           blank=True,
                           unique=True,
                           default=None)
    inauguracao = models.DateTimeField(default=datetime.datetime.now(),
                                       verbose_name="Data de Inauguração",
                                       help_text="Escolha uma data e hora")

    class Meta:
        abstract = False
        permissions = {
            ('reserve_estadio', 'can reserve Estadios')
        }

    def __str__(self):
        return self.nome

    def save(self, *args, **kargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(11))
        super().save(*args, **kargs)
