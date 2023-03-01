from django.db import models
from django.core.validators import *
# Create your models here.

class PersonAbstract(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    birth_day = models.DateField(verbose_name='Дата рождения', auto_now_add=True)
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телефон', max_length=50, blank=True, validators=[RegexValidator(
        regex=r'^\+[0-9]$',
        message='Номер телефона начинается со знака "+" и содержить только цифры'
    )])
    image = models.ImageField(verbose_name='Изображение', blank=True)

    class Meta:
        abstract = True

        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

