# Generated by Django 2.2.2 on 2021-06-18 20:47

from django.db import migrations, models
import django.utils.timezone
import iHerbServer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('avatar', models.ImageField(blank=True, default='/diplomv/user_avatars/default_avatar.png', null=True, upload_to='diplomv/user_avatars/', verbose_name='Фото')),
                ('uuid', models.CharField(max_length=255, verbose_name='UUID')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', iHerbServer.models.UserManager()),
            ],
        ),
    ]
