# Generated by Django 4.2.3 on 2023-07-31 05:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mtf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nombre')),
                ('max_men', models.PositiveSmallIntegerField(help_text='Máxima cantidad de hombres permitido para esta categoría.', verbose_name='Cantidad de hombres')),
                ('max_women', models.PositiveSmallIntegerField(help_text='Máxima cantidad de mujeres permitido para esta categoría.', verbose_name='Cantidad de mujeres')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table_comment': 'Categorías de evento.',
            },
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(help_text='Nombre completo del jurado. Ejemplo: Juan García.', verbose_name='Nombre completo')),
                ('instagram', models.CharField(max_length=30, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Juez',
                'verbose_name_plural': 'Jueces',
                'db_table_comment': 'Jueces de baile que evalúan las participaciones.',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nombre')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo')),
                ('instagram', models.CharField(max_length=30, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Patrocinante',
                'verbose_name_plural': 'Patrocinantes',
                'db_table_comment': 'Patrocinantes del evento.',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelTableComment(
            name='event',
            table_comment='Eventos de competencia de baile.',
        ),
        migrations.AlterField(
            model_name='event',
            name='instagram',
            field=models.CharField(max_length=30, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='event',
            name='logo',
            field=models.ImageField(upload_to='', verbose_name='Logo'),
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order', models.PositiveSmallIntegerField(help_text='Indica el orden de presentación de las categorías de este evento.', verbose_name='Orden de presentación')),
                ('date', models.DateField(verbose_name='Fecha de presentación de la categoría.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtf.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtf.event')),
            ],
            options={
                'verbose_name': 'Categoría de evento',
                'verbose_name_plural': 'Categorías del evento',
                'db_table': 'mtf_event_category',
                'db_table_comment': 'Categorías específicas para un evento dado.',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(through='mtf.EventCategory', to='mtf.category', verbose_name='Categorías'),
        ),
        migrations.AddField(
            model_name='event',
            name='judges',
            field=models.ManyToManyField(db_table='mtf_event_judge', to='mtf.judge', verbose_name='Jueces'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(db_table='mtf_event_sponsor', to='mtf.sponsor', verbose_name='Patrocinantes'),
        ),
        migrations.AddConstraint(
            model_name='eventcategory',
            constraint=models.UniqueConstraint(fields=('event', 'category'), name='event_category_event_category_uk', violation_error_message='Categoría ya asociada a este evento.'),
        ),
        migrations.AddConstraint(
            model_name='eventcategory',
            constraint=models.UniqueConstraint(fields=('event', 'order', 'date'), name='event_category_event_date_order_uk', violation_error_message='No puedes repetir el orden de presentación para este día.'),
        ),
    ]
