from django.db import models

# Para mostrar propiedades destacadas aunque no sea un buscador real aún
class PropiedadDestacada(models.Model):
    TIPO_CHOICES = [('Venta', 'Venta'), ('Alquiler', 'Alquiler')]
    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True)
    habitaciones = models.IntegerField()
    baños = models.IntegerField()

# Para generar confianza
class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    cargo = models.CharField(max_length=100, default="Cliente Satisfecho")

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Nombre de clase FontAwesome o similar")
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo