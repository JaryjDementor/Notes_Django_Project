from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.


def first_page(reqeust):
    return render(reqeust, "accounts/first_page.html")


def form_new_user(request):
    form = NewUserForm()
    return HttpResponseBadRequest(render(
        request=request,
        template_name="accounts/register.html",
        context={"register_form": form},
    ))


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            mail = order.email
            email_from_bd = User.objects.filter(email=mail)
            if email_from_bd:
                assert  HttpResponseBadRequest(form_new_user(request))
            else:
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return HttpResponseRedirect("accounts/view_notebooks")
    return HttpResponseBadRequest(form_new_user(request))


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect("accounts/view_notebooks")
    form = AuthenticationForm()
    return HttpResponseBadRequest(render(
        request=request,
        template_name="accounts/login.html",
        context={"login_form": form},
    ))


def logout_request(request):
    logout(request)
    return redirect("first_page")


def resset_password_request(request):
    id = request.user.id
    if id:
        return HttpResponseBadRequest(redirect("view notebooks"))
    else:
        if request.method == "POST":
            password_form = PasswordResetForm(request.POST)
            if password_form.is_valid():
                data = password_form.cleaned_data.get("email")
                user_email = User.objects.filter(Q(email=data))
                if user_email.exists():
                    for user in user_email:
                        subjects = "Password Resquest"
                        email_template_name = "accounts/password_messege.txt"
                        parameters = {
                            "email": user.email,
                            "domain": "127.0.0.1:8000",
                            "site_name": "Notes_project",
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "token": default_token_generator.make_token(user),
                            "protocol:": "http",
                        }
                        email = render_to_string(email_template_name, parameters)
                        try:
                            send_mail(
                                subjects, email, "", [user.email], fail_silently=False
                            )
                        except:
                            return HttpResponse("Invalid Header")
                        return redirect("succesful_send")

        else:
            password_form = PasswordResetForm()
        context = {
            "password_form": password_form,
        }
        return render(
            request=request,
            template_name="accounts/reset_password.html",
            context=context,
        )


def check_mail(request):
    return render(request=request, template_name="accounts/send_mail_succesful.html")
