# Generated by Django 4.2.11 on 2024-03-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0008_remove_like_management_userswholikeme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userswholikeme',
            name='user',
        ),
        migrations.RemoveField(
            model_name='whoilike',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like_Management',
        ),
        migrations.DeleteModel(
            name='UserswhoLikeMe',
        ),
        migrations.DeleteModel(
            name='WhoILike',
        ),
    ]