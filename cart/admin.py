from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cart.models import Cart


# Регистрация своих моделей в Админ-панели
admin.site.register(Cart, admin.ModelAdmin)
