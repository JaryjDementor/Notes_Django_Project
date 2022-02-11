from django.urls import path
from .views import *

urlpatterns = [
    path('', create, name='addnote'),
    path('/viewint_title', create, name='addnote'),
    ]

