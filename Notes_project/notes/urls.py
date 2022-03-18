from django.urls import path
from .views import (
    create,
    viewes_user_title,
    view_your_note,
    create_notebook,
    viewes_user_notebooks,
    viewes_notebook,
)

urlpatterns = [
    path("/view_notebooks", viewes_user_notebooks, name="view notebooks"),
    path("/notebook/<int:idnotebook>", viewes_notebook, name="notebook"),
    path("/create/<int:idnotebook>", create, name="add_note"),
    path(
        "/view_note/<int:idnotebook>/<int:id_note>", view_your_note, name="view_notess"
    ),
    path("/addnotebook", create_notebook, name="add_notebook"),
    path("/viewint_title", viewes_user_title, name="viewint_title"),
]
