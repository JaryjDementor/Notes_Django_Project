from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import NotesUser
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea, IntegerField


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# class NoteUserForm(ModelForm):
#     class Meta:
#         # model=NotesUser
#         fields=['id','title','text','data']
#
#         widgets= {
#             'id': IntegerField(attr={
#                 'class': 'form-control'
#             }),
#             'title': TextInput(attrs={
#                 'class':'form-control',
#                 'placeholder': 'Yor title'
#             }),
#             'content': Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Yor note'
#             }),
#             'data': DateTimeInput(attrs={
#                 'class': 'form-control'
#             })
#
#             }
#





