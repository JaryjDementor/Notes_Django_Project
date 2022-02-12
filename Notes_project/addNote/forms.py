
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea, IntegerField
from . import models



class NoteUserForm(ModelForm):
    class Meta:
        model=models.Create_base
        fields=['title', 'text']

        widgets= {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your note'
            }),
            'iduser': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'idUser'
            })

            }

