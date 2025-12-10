from django.contrib import admin
from .models import Quiz, Question, AnswerOption


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 3
    min_num = 1
    can_delete = True


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz")
    inlines = [AnswerOptionInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("question", "is_correct")
