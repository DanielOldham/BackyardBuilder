from django.db import models
from django.contrib.auth.models import User
from components.models import Case, Cooler, CPU, Graphics, Motherboard, PowerSupply, RAM, Storage


# Create your models here.
class Build(models.Model):
    name = models.CharField(max_length=75)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, default=None)
    cooler = models.ForeignKey(Cooler, on_delete=models.SET_NULL, null=True, default=None)
    cpu = models.ForeignKey(CPU, on_delete=models.SET_NULL, null=True, default=None)
    graphics = models.ForeignKey(Graphics, on_delete=models.SET_NULL, null=True, default=None)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True, default=None)
    powersupply = models.ForeignKey(PowerSupply, on_delete=models.SET_NULL, null=True, default=None)
    ram = models.ForeignKey(RAM, on_delete=models.SET_NULL, null=True, default=None)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.name
