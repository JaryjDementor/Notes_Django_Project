# Generated by Django 4.0.1 on 2022-03-22 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_id_notebook_alter_note_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 21, 27, 21, 176542)),
        ),
    ]
