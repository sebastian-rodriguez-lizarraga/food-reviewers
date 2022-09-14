from pyexpat import model
from django.db import models


class userlog(models.Model):
    nombre=models.CharField(max_length=60)
    _contraseña=models.CharField(max_length=50)

    def __str__(self):
        return(self.nombre)
