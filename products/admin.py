from django.contrib import admin
from products.models import Product, Stock


# Регистрация моделей на админ-панели
admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Stock, admin.ModelAdmin)