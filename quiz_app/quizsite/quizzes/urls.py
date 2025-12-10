from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    # ---- Quiz CRUD ----
    path('', views.quiz_list, name='quiz_list'),  # Root path shows all quizzes
    path('create/', views.quiz_create, name='quiz_create'),
    path('update/<int:pk>/', views.quiz_update, name='quiz_update'),
    path('delete/<int:pk>/', views.quiz_delete, name='quiz_delete'),

    # ---- Question CRUD ----
    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.question_create, name='question_create'),
    path('questions/update/<int:pk>/', views.question_update, name='question_update'),
    path('questions/delete/<int:pk>/', views.question_delete, name='question_delete'),

    # ---- Take Quiz ----
    path('<int:pk>/take/', views.quiz_take, name='quiz_take'),
    path('<int:pk>/submit/', views.quiz_submit, name='quiz_submit'),
]
