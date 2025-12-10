# quizzes/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Quiz, Question, AnswerOption

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text']  # quiz included

AnswerFormSet = inlineformset_factory(
    Question, AnswerOption,
    fields=['text', 'is_correct'],
    extra=2, can_delete=True
)
