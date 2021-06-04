from django.contrib import admin
from polls.models import Poll, Answer, Question, QuestionChoice


class PollAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'visible',
    )

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'poll',
        'type',
    )
    list_filter = ('poll',)

class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'text'
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'poll',
        'question',
        'choice',
    )
    list_filter = ('user',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
