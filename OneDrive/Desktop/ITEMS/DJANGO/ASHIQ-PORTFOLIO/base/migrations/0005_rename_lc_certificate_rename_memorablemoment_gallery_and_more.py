# Generated by Django 4.0.5 on 2022-11-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_icons_workedclub_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LC',
            new_name='Certificate',
        ),
        migrations.RenameModel(
            old_name='MemorableMoment',
            new_name='Gallery',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='me_info',
            new_name='current_qualification',
        ),
        migrations.AddField(
            model_name='profile',
            name='current_team',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workedclub',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
