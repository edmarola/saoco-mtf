# Generated by Django 4.2.3 on 2023-07-23 02:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(help_text='Indica la fecha de inicio del evento.', verbose_name='Fecha de inicio')),
                ('end_date', models.DateField(help_text='Indica la fecha de inicio del evento.', verbose_name='Fecha de fin')),
                ('name', models.CharField(help_text='Nombre correspondiente a la edición de este evento. Ejemplo: MTF 2023.', verbose_name='Nombre')),
                ('logo', models.URLField(help_text='URL del logo del evento.', verbose_name='Logo')),
                ('instagram', models.CharField(help_text='Cuenta de usuario de instagram. Ejemplo: @margaritatimbafest.', max_length=30, verbose_name='Instagram')),
            ],
        ),
    ]
