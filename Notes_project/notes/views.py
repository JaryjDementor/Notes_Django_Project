from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from .forms import NoteUserForm, NotebookForm
from .models import Note, Notebook


class Notebook_name_Update(UpdateView): #Yes
    model = Notebook
    template_name = "notes/update_name_notebook.html"

    form_class = NotebookForm


class Note_Update(UpdateView): #Yes
    model = Note
    template_name = "notes/update_note.html"

    form_class = NoteUserForm
    context_object_name = "note"


def check_log(id_user):
    if id_user:
        pass
    else:
        raise PermissionDenied()


def delete_notebook(request, idnotebook: int): #Yes
    Notebook.objects.filter(id=idnotebook).delete()
    return redirect("view notebooks")


def delete_note(request, idnotebook: int, idnote: int):
    Note.objects.filter(id=idnote).delete()
    return redirect("notebook", idnotebook)


def viewes_user_notebooks(request): #Yes
    idus = request.user.id
    id_staff = request.user.is_staff
    check_log(idus)
    db = Notebook.objects.all()
    namenotebook = Notebook.objects.filter(iduser=idus)
    data = {"info": namenotebook, "db": db, "id_staff": id_staff}
    return render(request, "notes/view_notebooks.html", context=data)


def create_notebook(request): #Yes
    idus = request.user.id
    check_log(idus)
    if request.method == "POST":
        form = NotebookForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.iduser = idus
            order.save()
            # url=reverse('view notebooks')
            return redirect("view notebooks")

    form = NotebookForm
    data = {"form": form}
    return render(request, "notes/create_notebook.html", data)


def viewes_notebook(request, idnotebook: int): #Yes
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

def view_your_note(request, idnotebook: int, idnote: int):
    idus = request.user.id
    check_log(idus)
    note = Note.objects.get(id=idnote, id_notebook=idnotebook)
    if int(note.iduser) == int(idus):
        return render(request, "notes/detail_note.html", context={"note": note})
    else:
        raise PermissionDenied()
