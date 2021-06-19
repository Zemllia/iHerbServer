from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, phone=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) if not phone else self.model(email=email, phone=phone,
                                                                                    **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, phone, **extra_fields)

    def create_superuser(self, email, password, phone=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, phone, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    phone = models.PositiveIntegerField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    avatar = models.ImageField(upload_to='iHerbServer/user_avatars/', null=True, blank=True, verbose_name='Фото',
                               default='/iHerbServer/user_avatars/default_avatar.png')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос", null=False)
    answers = models.ManyToManyField('Answer', related_name='Questions', verbose_name='Варианты ответов')
    priority = models.IntegerField(verbose_name='Приоритет вопроса (для порядка вопросов)', null=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ответ", null=False)
    tags_for_choose = models.ManyToManyField("BADTag", related_name='Answers',
                                             verbose_name='Тэги БАДов для подбора БАДа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class BAD(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название", null=False)
    description = models.TextField(verbose_name='Описание БАД')
    images = models.ManyToManyField('BADImage', related_name='BAD', verbose_name='Изображения для БАД', blank=True)
    shop_link = models.TextField(verbose_name='Ссылка на БАД в магазине iHerb')
    tags = models.ManyToManyField("BADTag", related_name='BADs', verbose_name='Теги')

    class Meta:
        verbose_name = 'БАД'
        verbose_name_plural = 'БАДы'


class BADImage(models.Model):
    image = models.ImageField(upload_to='iHerbServer/bad_images/', null=True, blank=True, verbose_name='Изображение',
                              default='/iHerbServer/bad_images/default_bad_image.png')

    class Meta:
        verbose_name = 'Изображение БАДа'
        verbose_name_plural = 'Изображения БАДов'


class BADTag(models.Model):
    name = models.CharField(verbose_name="Называние тега для пометки БАДа", max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг БАДа'
        verbose_name_plural = 'Тэги БАДов'
