# Generated by Django 4.1.5 on 2023-02-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='on_subject',
            field=models.ManyToManyField(related_name='student_subject', to='subjects.subject', verbose_name='Предмет'),
        ),
    ]