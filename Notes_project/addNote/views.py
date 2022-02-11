from django.shortcuts import render, redirect
from .forms import NoteUserForm
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
            return redirect()


        else:
            error= 'Not good form'
    form=NoteUserForm
    data={
        'form':form,
        'error': error
    }
    return render(request,'addNote/create.html',data)

