from django.db import models
from django.core.validators import MinValueValidator
from customers.models import Customer, Address
from products.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждён'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]

    order_id = models.AutoField(primary_key=True, verbose_name="Номер заказа")
    customer = models.ForeignKey(
        Customer,
        on_delete=models.RESTRICT,
        related_name='orders',
        verbose_name='Заказчик'
    )
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Общая сумма'
    )
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending',
        verbose_name='Статус заказа'
    )
    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='shipping_orders',
        verbose_name='Адрес доставки'
    )
    billing_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='billing_orders',
        verbose_name='Адрес для биллинга'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ #{self.order_id} от {self.order_date.date()}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена за единицу на момент заказа'
    )

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f'{self.quantity} × {self.product.name} в заказе #{self.order.order_id}'