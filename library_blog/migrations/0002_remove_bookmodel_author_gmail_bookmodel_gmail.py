# Generated by Django 5.1.4 on 2024-12-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='author_gmail',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='gmail',
            field=models.EmailField(max_length=254, null=True, verbose_name='Укажите эл.почту автора'),
        ),
    ]