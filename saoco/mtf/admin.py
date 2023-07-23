from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date", "logo", "instagram"]


admin.site.register(Event, EventAdmin)
