import uuid
from django.db import models


# Create your models here.
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
    )
    logo = models.ImageField(
        verbose_name="Logo",
        help_text="Imagen correspondiente al logo del evento.",
    )
    instagram = models.CharField(
        max_length=30,
        verbose_name="Instagram",
        help_text=(
            "Cuenta de usuario de instagram. Ejemplo: @margaritatimbafest."
        ),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
