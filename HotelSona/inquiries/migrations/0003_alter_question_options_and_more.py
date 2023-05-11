# Generated by Django 4.2.1 on 2023-05-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0002_alter_question_options_alter_question_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquiries.question')),
            ],
        ),
    ]
