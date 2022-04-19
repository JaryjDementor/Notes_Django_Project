from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .forms import NoteUserForm, NotebookForm
from .models import Note, Notebook
from random import randint



class Notebook_name_Update(UpdateView):
    model = Notebook
    template_name = "notes/update_name_notebook.html"

    form_class = NotebookForm


class Note_Update(UpdateView):
    model = Note
    template_name = "notes/update_note.html"

    form_class = NoteUserForm
    context_object_name = "note"


def check_log(id_user):
    if id_user:
        pass
    else:
        raise PermissionDenied()


def delete_notebook(request, idnotebook: int):
    Notebook.objects.filter(id=idnotebook).delete()
    return redirect("view notebooks")


def delete_note(request, idnotebook: int, idnote: int):
    Note.objects.filter(id=idnote).delete()
    return redirect("notebook", idnotebook)


def viewes_user_notebooks(request):
    idus = request.user.id
    id_staff = request.user.is_staff
    check_log(idus)
    db = Notebook.objects.all()
    namenotebook = Notebook.objects.filter(iduser=idus)
    data = {"info": namenotebook, "db": db, 'id_staff': id_staff}
    return render(request, "notes/view_notebooks.html", context=data)


def create_notebook(request):
    idus = request.user.id
    check_log(idus)
    if request.method == "POST":
        form = NotebookForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.iduser = idus
            order.save()
            return redirect("view notebooks")

    form = NotebookForm
    data = {"form": form}
    return render(request, "notes/create_notebook.html", data)


def viewes_notebook(request, idnotebook: int):
    idus = request.user.id
    check_log(idus)
    notebook = Notebook.objects.get(id=idnotebook)
    if int(notebook.iduser) == int(idus):
        title = Note.objects.filter(id_notebook=idnotebook)
        return render(
            request,
            "notes/notebook.html",
            context={"title": title, "idnotebook": idnotebook, "notebook": notebook},
        )
    else:
        raise PermissionDenied()


def create(request, idnotebook: int):
    idus = request.user.id
    check_log(idus)
    if request.method == "POST":
        form = NoteUserForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.iduser = request.user.id
            order.id_notebook = idnotebook
            order.save()
            return redirect("notebook", idnotebook)
    form = NoteUserForm
    data = {"form": form, "idnotebook": idnotebook}
    return render(request, "notes/create.html", data)


def viewes_user_title(request):
    idus = request.user.id
    check_log(idus)
    db = Note.objects.all()
    title = Note.objects.filter(iduser=idus)
    data = {"info": title, "db": db}
    return render(request, "notes/viewe_user_title.html", context=data)


def view_your_note(request, idnotebook: int, idnote: int):
    idus = request.user.id
    check_log(idus)
    note = Note.objects.get(id=idnote, id_notebook=idnotebook)
    if int(note.iduser) == int(idus):
        return render(request, "notes/detail_note.html", context={"note": note})
    else:
        raise PermissionDenied()
