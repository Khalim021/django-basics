# Generated by Django 3.1.7 on 2021-04-14 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210414_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='title',
            new_name='genre',
        ),
    ]