from django.urls import path, include
from products.views import ListProducts

"""
product_patterns = [
    path('', views.products),
    path('new/', views.new),
    path('top/', views.top),
]
"""
urlpatterns = [
    path('', ListProducts.as_view()),
]