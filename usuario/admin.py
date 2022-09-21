from django.contrib import admin
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UsuarioInLine (admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'

class CustomizedUserAdmin (UserAdmin):
    inlines= (UsuarioInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin )