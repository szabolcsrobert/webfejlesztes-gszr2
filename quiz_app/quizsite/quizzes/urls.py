from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/create/', views.quiz_create, name='quiz_create'),
    path('quizzes/update/<int:pk>/', views.quiz_update, name='quiz_update'),
    path('quizzes/delete/<int:pk>/', views.quiz_delete, name='quiz_delete'),

    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.question_create, name='question_create'),
    path('questions/update/<int:pk>/', views.question_update, name='question_update'),
    path('questions/delete/<int:pk>/', views.question_delete, name='question_delete'),
path('quiz/<int:pk>/take/', views.quiz_take, name='quiz_take'),
    path('quiz/<int:pk>/submit/', views.quiz_submit, name='quiz_submit'),
]
