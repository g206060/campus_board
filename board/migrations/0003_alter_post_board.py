# Generated by Django 3.2.18 on 2023-10-20 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.board', verbose_name='掲示板名'),
        ),
    ]
