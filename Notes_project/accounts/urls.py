from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (
    login_request,
    first_page,
    register_request,
    logout_request,
    resset_password_request,
    check_mail,
)

urlpatterns = [
    path("", first_page, name="first_page"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("reset_password", resset_password_request, name="reset"),
    path("succesful_send_mail", check_mail, name="succesful_send"),
    path(
        "reset_password_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_confirm.html",
            success_url=reverse_lazy("login"),
        ),
        name="password_confirm",
    ),
]
