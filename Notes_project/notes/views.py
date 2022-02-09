from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest

from .forms import NewUserForm
from django.contrib.auth import login, authenticate,models
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from .forms import NoteUserForm
# Create your views here.

# def create(request):
#     form=NoteUserForm
#
#     data={
#         'form':form
#     }
#     return render(request,'notes/create.html',data)

def idUser(request):
    id =request.user.id
    return id

def first_page(reqeust):
    return render(reqeust,'notes/first_page.html')

def hallo_world(request):
    a=request.user.get_username()
    id = request.user.id
    data={
        'info':id
    }
    return render(request,'notes/hamepage.html',context=data)




def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="notes/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")

                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="notes/login.html", context={"login_form":form})

# def id_user(username,password):


# def editor(request):
#     docid=int(request.Get.get('docid',0))
#     dokuments=Document.object.all()
#
#     context={
#         'docid':docid,
#         'dokuments': dokuments
#     }
#
#     return render(request,'editor.html',context=context)

def id():
    user = authenticate(username='Test', password='Maestro0507')
    return user
