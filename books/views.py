from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializer import BookSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer