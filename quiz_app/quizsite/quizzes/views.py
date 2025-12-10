from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def quiz_create(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('quiz_list')
    return render(request, 'quizzes/quiz_form.html', {'form': form})

def quiz_update(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizForm(request.POST or None, instance=quiz)
    if form.is_valid():
        form.save()
        return redirect('quiz_list')
    return render(request, 'quizzes/quiz_form.html', {'form': form})

def quiz_delete(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')
    return render(request, 'quizzes/quiz_confirm_delete.html', {'quiz': quiz})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quizzes/question_list.html', {'questions': questions})

def question_create(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, 'quizzes/question_form.html', {'form': form})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, 'quizzes/question_form.html', {'form': form})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'quizzes/question_confirm_delete.html', {'question': question})
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    return render(request, 'quizzes/quiz_take.html', {'quiz': quiz, 'questions': questions})
def quiz_submit(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()

    total = questions.count()
    correct = 0

    for question in questions:
        selected_option_id = request.POST.get(str(question.id))
        if not selected_option_id:
            continue  # Question was skipped

        try:
            selected_option = AnswerOption.objects.get(id=selected_option_id)
            if selected_option.is_correct:
                correct += 1
        except AnswerOption.DoesNotExist:
            pass

    percentage = round((correct / total) * 100, 2) if total > 0 else 0

    return render(request, 'quizzes/quiz_result.html', {
        'quiz': quiz,
        'total': total,
        'correct': correct,
        'percentage': percentage
    })
