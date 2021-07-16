from rest_framework import generics
from .models import Book
from project.serializers import BookSerializer

# Create your views here.


###  list books 

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


### Book details 
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer