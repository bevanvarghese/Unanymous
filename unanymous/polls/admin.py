from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Unanymous Admin'
admin.site.site_title = 'Unanymous Admin Area'
admin.site.index_title = 'Welcome to the Unanymous Admin Area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['published_on'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
