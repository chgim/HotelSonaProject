# Generated by Django 4.2.1 on 2023-06-18 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_reservation_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='room',
            name='availRoom',
        ),
    ]