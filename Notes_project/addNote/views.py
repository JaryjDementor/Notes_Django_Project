from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteUserForm
from .models import Create_base
from django.http import HttpResponse
# Create your views here.


def create(request):
    error=''
    id = request.user.id
    if request.method == 'POST':

        form = NoteUserForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.iduser=request.user.id
            order.save()
            return redirect("viewint_title")


        else:
            error= 'Not good form'
    form=NoteUserForm
    data={
        'form':form,
        'error': error
    }
    return render(request,'addNote/create.html',data)


def viewes_user_title(request):
    db=Create_base.objects.all()
    idus=request.user.id
    title = Create_base.objects.filter(iduser=idus)
    data={
        'info': title,
        'db': db
    }
    return render(request,'addNote/viewe_user_title.html',context=data)

def view_your_note(request,id_note: int):
    note=Create_base.objects.get(id=id_note)
    # movie = get_object_or_404(Create_base)
    return render(request,'addNote/detail_note.html',context={'note':note})