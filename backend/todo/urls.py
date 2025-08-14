from django.urls import path
from .views import DetailsTodo,ListTodo

urlpatterns = [
    path('<int:pk>/',DetailsTodo.as_view()),
    path('',ListTodo.as_view())
]
