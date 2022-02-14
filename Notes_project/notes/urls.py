from django.urls import path
from .views import *

urlpatterns = [
    path('', first_page,name='first_page'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),

]
