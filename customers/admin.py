from django.contrib import admin
from customers.models import Customer, Address


# Регистрация своих моделей в Админ-панели
admin.site.register(Customer, admin.ModelAdmin)
admin.site.register(Address, admin.ModelAdmin)