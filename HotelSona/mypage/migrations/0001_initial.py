# Generated by Django 4.2.1 on 2023-06-18 20:49

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.userprofile',),
        ),
    ]
