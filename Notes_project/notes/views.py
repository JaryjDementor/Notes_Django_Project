from django.shortcuts import render, redirect
from .forms import NoteUserForm
from .models import Note

# Create your views here.


def create(request):
    idus = request.user.id
    if idus:
        if request.method == "POST":

            form = NoteUserForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.iduser = request.user.id
                order.save()
                return redirect("viewint_title")

        form = NoteUserForm
        data = {"form": form}
        return render(request, "notes/create.html", data)
    else:
        return redirect("first_page")


def viewes_user_title(request):
    idus = request.user.id
    if idus:
        db = Note.objects.all()
        title = Note.objects.filter(iduser=idus)
        data = {"info": title, "db": db}
        return render(request, "notes/viewe_user_title.html", context=data)
    else:
        return redirect("first_page")


def view_your_note(request, id_note: int):
    idus = request.user.id
    if idus:
        note = Note.objects.get(id=id_note)
        return render(request, "notes/detail_note.html", context={"note": note})
    else:
        return redirect("first_page")
