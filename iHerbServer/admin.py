from django.contrib import admin
from .models import User, BAD, BADTag, BADImage, Question, Answer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone'
    ]


@admin.register(BAD)
class BADAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(BADImage)
class BADImageAdmin(admin.ModelAdmin):
    list_display = [

    ]


@admin.register(BADTag)
class BADTagAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [

    ]
