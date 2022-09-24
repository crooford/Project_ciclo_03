from django.contrib import admin
# Register your models here.
from .models import Menu, Mesas , Orden

admin.site.register(Menu)
admin.site.register(Mesas)
admin.site.register(Orden)