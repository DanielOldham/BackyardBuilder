from django.contrib import admin
from .models import CPU, RAM, Graphics, Case, Motherboard, Storage, PowerSupply, Cooler

# Register your models here.
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Graphics)
admin.site.register(Case)
admin.site.register(Motherboard)
admin.site.register(Storage)
admin.site.register(PowerSupply)
admin.site.register(Cooler)
