from django.db.models import Model, CharField, DateTimeField
from datetime import datetime


# Create your models here.


class Notebook(Model):
    name_notebook = CharField("Title", max_length=100)
    iduser = CharField("idUser", max_length=5)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return f" {self.name_notebook}"


class Note(Model):
    title = CharField("Title", max_length=100)
    text = CharField("Your note", max_length=1000)
    data = DateTimeField(default=datetime.now())
    iduser = CharField("idUser", max_length=5)
    id_notebook = CharField("idUser", max_length=5)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return f" {self.title} {self.text} {self.data}"
