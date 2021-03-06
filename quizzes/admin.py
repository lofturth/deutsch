from django.contrib import admin

from .models import Verb, Sentence, Quiz, VerbDetail

class VerbAdmin(admin.ModelAdmin):
    list_display = ['infinitive', 'ich_present', 'du_present', 'er_present', 'wir_present', 'ihr_present', 'sie_present']
admin.site.register(Verb, VerbAdmin)


class VerbDetailAdmin(admin.ModelAdmin):
    list_display = ['position']
admin.site.register(VerbDetail, VerbDetailAdmin)


class SentenceAdmin(admin.ModelAdmin):
    list_display = ['text']
admin.site.register(Sentence, SentenceAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
admin.site.register(Quiz, QuizAdmin)

