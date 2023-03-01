# Generated by Django 4.1.5 on 2023-03-01 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_alter_testimonial_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='phone',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Номер телефона начинается со знака "+" и содержить только цифры', regex='^\\+[0-9]$')], verbose_name='Телефон'),
        ),
    ]
