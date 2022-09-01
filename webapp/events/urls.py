from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path("index", views.index, name="index"),
    path("event", views.event, name="event"),
    path("details/<int:event_id>/", views.detail, name="detail"),
    path("new", views.new_event, name="new_event"),
    path("edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/<int:event_id>/", views.delete_event, name="delete_event"),
]
