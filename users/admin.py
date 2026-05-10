from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Добавляем модель Пользователя на админ-панель
admin.site.register(User, UserAdmin)