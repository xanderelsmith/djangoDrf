from django.shortcuts import render
from rest_framework import generics

from todo.models import Todo
from todo.serializers import TodoSerializer
# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodoSerializer

class DetailsTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class =TodoSerializer