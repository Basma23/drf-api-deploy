from django.urls import path
from .views import BooksList, BookDetails

urlpatterns = [
    path('', BooksList.as_view(), name='books'),
    path('<int:pk>/', BookDetails.as_view(), name='book_details') 
]