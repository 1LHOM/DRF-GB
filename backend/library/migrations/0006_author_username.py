# Generated by Django 3.2.12 on 2022-02-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_author_birthday_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=64, null=True),
        ),
    ]