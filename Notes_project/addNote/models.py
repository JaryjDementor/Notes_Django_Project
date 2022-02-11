
from django.db.models import Model, IntegerField,CharField,DateTimeField

# Create your models here.


class Create_base(Model):
    title=CharField('Title',max_length=100)
    text=CharField('Your note', max_length=255)
    data=DateTimeField('Date yor note')
    iduser=CharField('idUser',max_length=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

