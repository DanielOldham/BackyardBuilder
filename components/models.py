from django.db import models


# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(default='component_images/default_component.png', upload_to='component_images')
    link = models.URLField()

    def __str__(self):
        return self.name


class CPU(Component):
    # speed is in GHz
    speed = models.FloatField()


class RAM(Component):
    # speed is in GHz
    speed = models.FloatField()
    # size is in GBytes
    size = models.FloatField()


class Graphics(Component):
    # amount of vram in GBytes
    size = models.FloatField()


class Case(Component):
    color = models.CharField(max_length=50)


class Motherboard(Component):
    socket = models.CharField(max_length=50)


class Storage(Component):
    # size is in GBytes
    size = models.FloatField()


class PowerSupply(Component):
    # power is in Watts
    power = models.IntegerField()


class Cooler(Component):
    type = models.CharField(max_length=50)
