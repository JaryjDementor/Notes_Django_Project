from django.urls import path
from .views import *

urlpatterns = [
    path('', create, name='addnote'),
    path('/viewint_title', viewes_user_title, name='viewint_title'),
    path('/view_note/<int:id_note>', view_your_note, name='view_notess'),
    ]

