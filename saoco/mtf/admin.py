from django.contrib import admin
from .models import Event, Judge, Sponsor, Category, EventCategory


# Register your models here.
class EventCategoryInline(admin.TabularInline):
    model = EventCategory
    extra = 1
    ordering = ("order",)


class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date", "logo", "instagram"]
    inlines = (EventCategoryInline,)


admin.site.register(Event, EventAdmin)
admin.site.register(Judge)
admin.site.register(Sponsor)
admin.site.register(Category)
