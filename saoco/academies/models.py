from django.db import models


# Create your models here.
class Academy(models.Model):
    name = models.CharField("Nombre de la academia", max_length=128)
    manager_id_document = models.IntegerField(
        "Cédula del director", unique=True
    )
    manager_full_name = models.CharField(
        "Nombre completo del director", max_length=128
    )
    created_at = models.DateTimeField("Fecha de inscripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Academia"
        verbose_name_plural = "Academias"


class Dancer(models.Model):
    class DancerShirtSize(models.TextChoices):
        XS = "xs"
        S = "s"
        M = "m"
        L = "l"
        XL = "xl"

    class DancerGender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    id_document = models.IntegerField("Cédula", unique=True)
    full_name = models.CharField("Nombre completo", max_length=128)
    birthday = models.DateField("Fecha de nacimiento")
    shirt_size = models.CharField(
        "Talla de franela",
        max_length=2,
        choices=DancerShirtSize.choices,
        default=DancerShirtSize.M,
    )
    gender = models.CharField(
        "Género", max_length=6, choices=DancerGender.choices
    )
    academy = models.ForeignKey(Academy, on_delete=models.RESTRICT)

    def __str__(self):
        return "%s %s" % (self.id_document, self.full_name)

    class Meta:
        verbose_name = "Bailarín"
        verbose_name_plural = "Bailarines"
