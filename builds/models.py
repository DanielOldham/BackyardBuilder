from django.db import models
from django.contrib.auth.models import User
from components.models import Component, Case, Cooler, CPU, Graphics, Motherboard, PowerSupply, RAM, Storage


# Create your models here.
class Build(models.Model):
    name = models.CharField(max_length=75, default='My PC Plan')
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

    def total_price(self):
        total_price = 0
        components = []

        # make sure values aren't none to avoid ObjectDoesNotExist
        if self.case is not None:
            components.append(self.case)
        if self.cooler is not None:
            components.append(self.cooler)
        if self.cpu is not None:
            components.append(self.cpu)
        if self.graphics is not None:
            components.append(self.graphics)
        if self.motherboard is not None:
            components.append(self.motherboard)
        if self.powersupply is not None:
            components.append(self.powersupply)
        if self.ram is not None:
            components.append(self.ram)
        if self.storage is not None:
            components.append(self.storage)

        for component in components:
            total_price += component.price

        return round(total_price, 2)

    def component_count(self):
        count = 0

        if self.case is not None:
            count += 1
        if self.cooler is not None:
            count += 1
        if self.cpu is not None:
            count += 1
        if self.graphics is not None:
            count += 1
        if self.motherboard is not None:
            count += 1
        if self.powersupply is not None:
            count += 1
        if self.ram is not None:
            count += 1
        if self.storage is not None:
            count += 1

        return count
