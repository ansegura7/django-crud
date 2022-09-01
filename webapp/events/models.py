import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Category data model
class Category(models.Model):

    # Model variables
    name = models.CharField(max_length=50)

    # To String
    def __str__(self):
        return self.name


# Event data model
class Event(models.Model):

    # Model variables
    event_name = models.CharField(max_length=100)
    event_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    event_place = models.CharField(max_length=100)
    event_address = models.CharField(max_length=200)
    date_start = models.DateTimeField("Start date")
    date_end = models.DateTimeField("End date")
    event_virtual = models.BooleanField("Virtual event?", default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="admin")

    # To String
    def __str__(self):
        return self.event_name


# SignUpForm data model
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
