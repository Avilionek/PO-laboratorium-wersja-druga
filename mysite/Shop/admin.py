from django.contrib import admin
from .models import PC, HardDrive
from .models import GraphicsCard

admin.site.register(PC)
admin.site.register(GraphicsCard)
admin.site.register(HardDrive)
