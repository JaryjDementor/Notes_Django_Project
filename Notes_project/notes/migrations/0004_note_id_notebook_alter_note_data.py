# Generated by Django 4.0.1 on 2022-03-14 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notebook_alter_note_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='id_notebook',
            field=models.CharField(default=0, max_length=5, verbose_name='idUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 18, 20, 8, 762510)),
        ),
    ]
