from django.db import models
from .validators import validate_IMO


class Port(models.Model):
    name = models.CharField(max_length=200)
    locode = models.CharField(max_length=5)
    callCount = models.IntegerField(name='call_count', default=0)
    moveCount = models.IntegerField(name='move_count', default=0)
    #TODO: timezone
    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=200)
    imo = models.IntegerField(validators=[validate_IMO])
    def __str__(self):
        return self.name
        
                

class Call(models.Model):
    num = models.IntegerField()
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    eta = models.DateTimeField(null=True, blank=True)
    etd = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return str(self.num)

class Move(models.Model):
    num = models.IntegerField(default = 0)
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    prevMove = models.ForeignKey("self", on_delete=models.PROTECT)
    targetBerth = models.CharField(name='target_berth', max_length=10) 
    def __str__(self):
        return str(self.num)
