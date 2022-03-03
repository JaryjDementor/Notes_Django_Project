
from django.shortcuts import render, redirect
from .forms import NoteUserForm
from .models import Note
# Create your views here.


def create(request):
    if request.method == 'POST':

        form = NoteUserForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.iduser=request.user.id
            order.save()
            return redirect("viewint_title")

    form=NoteUserForm
    data={
        'form':form
    }
    return render(request,'notes/create.html',data)


def viewes_user_title(request):
    db=Note.objects.all()
    idus=request.user.id
    title = Note.objects.filter(iduser=idus)
    data={
        'info': title,
        'db': db
    }
    return render(request,'notes/viewe_user_title.html',context=data)

def view_your_note(request,id_note: int):
    note=Note.objects.get(id=id_note)
    # movie = get_object_or_404(Create_base)
    return render(request,'notes/detail_note.html',context={'note':note})