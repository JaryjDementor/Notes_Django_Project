from django.forms import ModelForm, TextInput, Textarea
from . import models


class NotebookForm(ModelForm):
    class Meta:
        model = models.Notebook
        fields = ["name_notebook"]

        widgets = {
            "name_notebook": TextInput(
                attrs={"class": "form-control", "placeholder": "name notebook"}
            ),
            "iduser": TextInput(
                attrs={"class": "form-control", "placeholder": "idUser"}
            ),
        }


class NoteUserForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ["title", "text"]

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Your note"}
            ),
            "iduser": TextInput(
                attrs={"class": "form-control", "placeholder": "idUser"}
            ),
        }
