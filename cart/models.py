from django.db import models
from django.core.validators import MinValueValidator
from customers.models import Customer
from products.models import Product


class Cart(models.Model):
    """
    Модель корзины заказов
    """
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Владелец корзины'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина клиента {self.customer}'


class CartItem(models.Model):
    """
    Вспомогательная модель для корзины заказов
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Корзина'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
        unique_together = ('cart', 'product')

    def __str__(self):
        return f'{self.quantity} × {self.product.name}'# ×