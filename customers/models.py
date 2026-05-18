from django.db import models


class Customer(models.Model):
    """
    Модель клиентов.
    """
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(
        max_length=100,
        verbose_name='Отчество',
        blank=True,
        null=True
    )
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    registration_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'



class Address(models.Model):
    """
    Модель хранения адреса покупателей
    """
    ADDRESS_TYPE_CHOICES = [
        ('shipping', 'Доставка'),
        ('billing', 'Биллинг'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name='Клиент'
    )
    address_type = models.CharField(
        max_length=20,
        choices=ADDRESS_TYPE_CHOICES,
        default='shipping',
        verbose_name='Тип адреса'
    )
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    apartment_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Номер квартиры'
    )
    postal_code = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Почтовый индекс'
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'