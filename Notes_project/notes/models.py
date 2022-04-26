from django.db.models import Model, CharField, DateTimeField
from datetime import datetime


# Create your models here.


class Notebook(Model):
    name_notebook = CharField("name_notebook", max_length=100)
    iduser = CharField("iduser", max_length=5)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return f"/accounts/notebook/{self.id}"

    def __str__(self):
        return f" {self.name_notebook}"


class Note(Model):
    title = CharField("title", max_length=100)
    text = CharField("text", max_length=1000)
    data = DateTimeField(default=datetime.now())
    iduser = CharField("iduser", max_length=5)
    id_notebook = CharField("id_notebook", max_length=5)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return f"/accounts/view_note/{self.id_notebook}/{self.id}"

    def __str__(self):
        return f" {self.title} {self.text} {self.data}"
