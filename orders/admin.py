from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from orders.models import Order


# Регистрация своих моделей в Админ-панели
admin.site.register(Order, admin.ModelAdmin)
