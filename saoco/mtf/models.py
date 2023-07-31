import uuid
from django.db import models


# Create your models here.
class Judge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(
        verbose_name="Nombre completo",
        help_text="Nombre completo del jurado. Ejemplo: Juan García.",
    )
    instagram = models.CharField(
        max_length=30,
        verbose_name="Instagram",
    )

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Juez"
        verbose_name_plural = "Jueces"
        db_table_comment = "Jueces de baile que evalúan las participaciones."


class Sponsor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        verbose_name="Nombre",
    )
    logo = models.ImageField(
        verbose_name="Logo",
    )
    instagram = models.CharField(
        max_length=30,
        verbose_name="Instagram",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Patrocinante"
        verbose_name_plural = "Patrocinantes"
        db_table_comment = "Patrocinantes del evento."


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        verbose_name="Nombre",
    )
    max_men = models.PositiveSmallIntegerField(
        verbose_name="Cantidad de hombres",
        help_text="Máxima cantidad de hombres permitido para esta categoría.",
    )
    max_women = models.PositiveSmallIntegerField(
        verbose_name="Cantidad de mujeres",
        help_text="Máxima cantidad de mujeres permitido para esta categoría.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        db_table_comment = "Categorías de evento."


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField(
        verbose_name="Fecha de inicio",
        help_text="Indica la fecha de inicio del evento.",
    )
    end_date = models.DateField(
        verbose_name="Fecha de fin",
        help_text="Indica la fecha de inicio del evento.",
    )
    name = models.CharField(
        verbose_name="Nombre",
        help_text=(
            "Nombre correspondiente a la edición de este evento. Ejemplo: MTF"
            " 2023."
        ),
        unique=True,
    )
    logo = models.ImageField(verbose_name="Logo", null=True, blank=True)
    instagram = models.CharField(
        max_length=30, verbose_name="Instagram", null=True, blank=True
    )
    judges = models.ManyToManyField(
        Judge, db_table="mtf_event_judge", verbose_name="Jueces", blank=True
    )
    sponsors = models.ManyToManyField(
        Sponsor,
        db_table="mtf_event_sponsor",
        verbose_name="Patrocinantes",
        blank=True,
    )
    categories = models.ManyToManyField(
        Category,
        through="EventCategory",
        verbose_name="Categorías",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        db_table_comment = "Eventos de competencia de baile."


class EventCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(
        verbose_name="Orden de presentación",
        help_text=(
            "Indica el orden de presentación de las categorías de este evento."
        ),
    )
    date = models.DateField(
        verbose_name="Fecha de presentación de la categoría.",
    )

    class Meta:
        verbose_name = "Categoría de evento"
        verbose_name_plural = "Categorías del evento"
        db_table = "mtf_event_category"
        db_table_comment = "Categorías específicas para un evento dado."
        constraints = [
            models.UniqueConstraint(
                name="event_category_event_category_uk",
                fields=["event", "category"],
                violation_error_message="Categoría ya asociada a este evento.",
            ),
            models.UniqueConstraint(
                name="event_category_event_date_order_uk",
                fields=["event", "order", "date"],
                violation_error_message=(
                    "No puedes repetir el orden de presentación para este día."
                ),
            ),
        ]
