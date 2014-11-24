from django.contrib import admin

from .models import Question, Answer, WrongAnswer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'question']

admin.site.register(Answer, AnswerAdmin)

# Register your models here.
class WrongAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'wrongAnswer', 'question']

admin.site.register(WrongAnswer, WrongAnswerAdmin)