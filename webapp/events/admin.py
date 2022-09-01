from django.contrib import admin

from .models import Category, Event


class EventAdmin(admin.ModelAdmin):

    list_display = (
        "event_name",
        "event_category",
        "event_address",
        "date_start",
        "event_virtual",
        "created_by",
        "date_created",
    )
    list_filter = ["date_start"]
    fieldsets = [
        (None, {"fields": ["event_name"]}),
        (
            "Event information",
            {
                "fields": [
                    "event_category",
                    "event_place",
                    "event_address",
                    "date_start",
                    "date_end",
                    "event_virtual",
                    "created_by",
                ]
            },
        ),
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Event, EventAdmin)
