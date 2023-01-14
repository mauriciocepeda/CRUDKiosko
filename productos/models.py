from django.db import models


class Producto(models.Model):
    marca=models.CharField(max_length=200)
    categoria=models.CharField(max_length=200)
    precio=models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.marca} {self.categoria}: ${self.precio}"