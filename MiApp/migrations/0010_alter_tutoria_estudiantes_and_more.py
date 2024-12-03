# Generated by Django 5.1.3 on 2024-12-02 23:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0009_alter_tutoria_unidad_duracion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoria',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, related_name='tutorias', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutoria',
            name='unidad_duracion',
            field=models.CharField(choices=[('min', 'Minutos'), ('hr', 'Horas'), ('day', 'Días'), ('wk', 'Semanas')], default='min', max_length=3),
        ),
    ]
