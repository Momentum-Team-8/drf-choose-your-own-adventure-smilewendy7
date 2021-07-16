from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework import permissions 
from project.serializers import BookSerializer
from .models import Book

# Create your views here.


###  list books ---- and add/create

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


### Book details 
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    ### only admin and update and delete ... 
    permission_classes = (permissions.IsAdminUser, )

    queryset = Book.objects.all()
    serializer_class = BookSerializer



#### list all featured books
class FeaturedList(ListAPIView): 
    ### return a singal/list of objects
    queryset  = Book.objects.filter(featured=True)
    serializer_class = BookSerializer
    pagination_class = None