from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from books.models import Book
from .serializers import BooksSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    # for allowiing all users to access the api
    permission_classes = [AllowAny]