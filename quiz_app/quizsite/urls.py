from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the quizzes app URLs
    path('', include('quizzes.urls', namespace='quizzes')),
]
