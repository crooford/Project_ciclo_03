from django.contrib import admin
# Register your models here.
from .models import IdOrden, Menu, Usuario , Mesas , Ordenmesas
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Menu)
class UsuarioInLine (admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'

class CustomizedUserAdmin (UserAdmin):
    inlines= (UsuarioInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin )
admin.site.register(Mesas)
admin.site.register(IdOrden)
admin.site.register(Ordenmesas)