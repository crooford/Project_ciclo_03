from django.contrib import admin
# Register your models here.
from .models import Menu, Usuario , Mesas , Ordenplato, Ordenmesa , Ordenmesas
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
admin.site.register(Ordenmesa)
admin.site.register(Ordenplato)
admin.site.register(Ordenmesas)