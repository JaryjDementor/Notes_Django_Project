
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea, IntegerField
from . import models



class NoteUserForm(ModelForm):
    class Meta:
        model=models.Create_base
        fields=['title', 'text', 'data']

        widgets= {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your note'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control'
            }),
            'iduser': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'idUser'
            })

            }

