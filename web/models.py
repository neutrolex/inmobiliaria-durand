from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Nombre de clase FontAwesome o similar")
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo