# quizzes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, AnswerOption
from .forms import QuizForm, QuestionForm, AnswerFormSet

# ---- Quizzes ----
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def quiz_create(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('quizzes:quiz_list')
    return render(request, 'quizzes/quiz_form.html', {'form': form})

def quiz_update(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizForm(request.POST or None, instance=quiz)
    if form.is_valid():
        form.save()
        return redirect('quizzes:quiz_list')
    return render(request, 'quizzes/quiz_form.html', {'form': form})

def quiz_delete(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quizzes:quiz_list')
    return render(request, 'quizzes/quiz_confirm_delete.html', {'quiz': quiz})

# ---- Questions ----
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quizzes/question_list.html', {'questions': questions})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        formset = AnswerFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            question = form.save()
            formset.instance = question
            formset.save()
            return redirect('quizzes:question_list')
    else:
        form = QuestionForm()
        formset = AnswerFormSet()

    return render(request, 'quizzes/question_form.html', {'form': form, 'formset': formset})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = AnswerFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('quizzes:question_list')
    else:
        form = QuestionForm(instance=question)
        formset = AnswerFormSet(instance=question)
    return render(request, 'quizzes/question_form.html', {'form': form, 'formset': formset})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('quizzes:question_list')
    return render(request, 'quizzes/question_confirm_delete.html', {'question': question})

# ---- Take Quiz ----
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    return render(request, 'quizzes/quiz_take.html', {'quiz': quiz, 'questions': questions})

def quiz_submit(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    total = questions.count()
    correct = 0
    results = []

    for question in questions:
        selected_option_id = request.POST.get(str(question.id))
        try:
            selected_option = AnswerOption.objects.get(id=selected_option_id)
            is_correct = selected_option.is_correct
        except:
            selected_option = None
            is_correct = False

        results.append({'question': question, 'selected': selected_option, 'correct': is_correct})
        if is_correct:
            correct += 1

    percentage = round((correct / total) * 100, 2) if total else 0

    return render(request, 'quizzes/quiz_result.html', {
        'quiz': quiz,
        'total': total,
        'correct': correct,
        'percentage': percentage,
        'results': results
    })
