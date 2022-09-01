from django import forms
from django.contrib.admin import widgets
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "event_name",
            "event_category",
            "event_place",
            "event_address",
            "date_start",
            "date_end",
            "event_virtual",
        )
        widgets = {
            "date_start": forms.DateTimeInput(attrs={"class": "datetime-input"}),
            "date_end": forms.DateTimeInput(attrs={"class": "datetime-input"}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
