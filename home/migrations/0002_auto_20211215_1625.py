# Generated by Django 3.2.9 on 2021-12-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='father_name',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='cgpa',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='student',
            name='sap',
            field=models.IntegerField(default=15),
        ),
    ]