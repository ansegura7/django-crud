import django_tables2 as tables
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import EventForm
from .models import Event, SignUpForm

# Class variables
loginErrorPage = "events/login_error.html"

# SignUp view - Create a new user
def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect("/events/index")
    else:
        form = SignUpForm()

    return render(request, "events/signup.html", {"form": form})


# Index view
def index(request):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        curr_username = request.user
        latest_event_list = Event.objects.filter(created_by=curr_username).order_by("-date_created")
        context = {"latest_event_list": latest_event_list}

        # Do something for authenticated users.
        return render(request, "events/index.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# List of Events view
def event(request):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        curr_username = request.user
        latest_event_list = Event.objects.filter(created_by=curr_username).order_by("-date_created")
        context = {"latest_event_list": latest_event_list}

        return render(request, "events/event.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# Event details view
def detail(request, event_id):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        event = get_object_or_404(Event, pk=event_id)
        context = {"event": event}

        return render(request, "events/detail.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# Create a New Event
def new_event(request):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        if request.method == "POST":
            curr_username = request.user
            form = EventForm(request.POST)

            if form.is_valid():
                curr_event = form.save(commit=False)
                curr_event.created_by = curr_username
                curr_event.save()

                return redirect("/events/event")
        else:
            form = EventForm()
            context = {"form": form}

        return render(request, "events/new_event.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# Edit an existed Event
def edit_event(request, event_id):

    # Session validation
    if request.user.is_authenticated:
        event = get_object_or_404(Event, pk=event_id)

        # Do something for authenticated users.
        if request.method == "POST":
            curr_username = request.user
            form = EventForm(request.POST, instance=event)

            if form.is_valid():
                curr_event = form.save(commit=False)
                curr_event.save()

                return redirect("/events/event")
        else:
            form = EventForm(instance=event)
            context = {"form": form}

        return render(request, "events/edit_event.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# Delete a Event
def delete_event(request, event_id):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        event = get_object_or_404(Event, pk=event_id)

        if request.method == "POST":

            event.delete()
            return redirect("/events/event")
        else:
            context = {"event": event}
            return render(request, "events/delete_event.html", context)
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)


# Delete a Event
def delete_object(request, event_id):

    # Session validation
    if request.user.is_authenticated:

        # Do something for authenticated users.
        object = get_object_or_404(Event, pk=event_id)
        object.delete()
        return redirect("/events/event")
    else:
        # Do something for anonymous users.
        return render(request, loginErrorPage)
