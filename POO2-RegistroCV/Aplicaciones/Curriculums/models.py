from django.db import models
from datetime import date

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class CV(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='fotos/')

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
