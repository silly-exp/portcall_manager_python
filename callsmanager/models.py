from django.db import models
from . validators import validate_IMO


class Port(models.Model):
    name = models.CharField(max_length=200)
    locode = models.CharField(max_length=5)
    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=200)
    imo = models.IntegerField(validators=[validate_IMO])
    def __str__(self):
        return self.name
        
                

class Call(models.Model):
    num = models.CharField(max_length=15)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    eta = models.DateTimeField(null=True, blank=True)
    etd = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.num

