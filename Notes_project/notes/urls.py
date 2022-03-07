from django.urls import path
from .views import create, viewes_user_title, view_your_note

urlpatterns = [
    path("", create, name="addnote"),
    path("/viewint_title", viewes_user_title, name="viewint_title"),
    path("/view_note/<int:id_note>", view_your_note, name="view_notess"),
]
