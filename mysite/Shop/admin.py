from django.contrib import admin
from .models import PC, Design, HardDrive
from .models import GraphicsCard

admin.site.register(PC)
admin.site.register(GraphicsCard)
admin.site.register(HardDrive)
admin.site.register(Design)
