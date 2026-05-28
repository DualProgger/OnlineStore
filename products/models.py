from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Модель хранения продуктов магазина
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена'
    )
    #image_url = models.URLField(blank=True, verbose_name='URL изображения')
    image = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name



class Stock(models.Model):
    """
    Модель склада товаров
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')

    class Meta:
        verbose_name = 'Запасы'
        verbose_name_plural = 'Запасы'

    def __str__(self):
        return f'{self.product.name}: {self.quantity} шт.'