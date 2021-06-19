# Generated by Django 2.2.2 on 2021-06-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iHerbServer', '0003_auto_20210619_0653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='bad',
            options={'verbose_name': 'БАД', 'verbose_name_plural': 'БАДы'},
        ),
        migrations.AlterModelOptions(
            name='badimage',
            options={'verbose_name': 'Изображение БАДа', 'verbose_name_plural': 'Изображения БАДов'},
        ),
        migrations.AlterModelOptions(
            name='badtag',
            options={'verbose_name': 'Тэг БАДа', 'verbose_name_plural': 'Тэги БАДов'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(related_name='users', to='iHerbServer.BADTag', verbose_name='Теги для пользователя'),
        ),
        migrations.AlterField(
            model_name='bad',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='BAD', to='iHerbServer.BADImage', verbose_name='Изображения для БАД'),
        ),
    ]
