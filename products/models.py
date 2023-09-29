from django.db import models
from core.validators import check_phonenum
from core.abstract_models import Abstract


class Product(Abstract):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Owner(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.EmailField()
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum]
    )
    default_product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="%(class)s_product"
    )

    class Meta:
        ordering = ['second_name']
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    def __str__(self):
        return self.name


