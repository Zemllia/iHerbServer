# Generated by Django 2.2.2 on 2021-06-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iHerbServer', '0002_auto_20210619_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ответ')),
            ],
        ),
        migrations.CreateModel(
            name='BADImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='/iHerbServer/bad_images/default_bad_image.png', null=True, upload_to='iHerbServer/bad_images/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='BADTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Называние тега для пометки БАДа')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('priority', models.IntegerField(verbose_name='Приоритет вопроса (для порядка вопросов)')),
                ('answers', models.ManyToManyField(related_name='Questions', to='iHerbServer.Answer', verbose_name='Варианты ответов')),
            ],
        ),
        migrations.CreateModel(
            name='BAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание БАД')),
                ('shop_link', models.TextField(verbose_name='Ссылка на БАД в магазине iHerb')),
                ('images', models.ManyToManyField(related_name='BAD', to='iHerbServer.BADImage', verbose_name='Изображения для БАД')),
                ('tags', models.ManyToManyField(related_name='BADs', to='iHerbServer.BADTag', verbose_name='Теги')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='tags_for_choose',
            field=models.ManyToManyField(related_name='Answers', to='iHerbServer.BADTag', verbose_name='Тэги БАДов для подбора БАДа'),
        ),
    ]
