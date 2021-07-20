from django.db.models import Q
## search
from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)
from django.db.models import query
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.permissions import(
    AllowAny,
    IsAdminUser,
)
from project.serializers import BookDetailSerializer,BookCreateSerializer
from .models import Book
from project.pagination import BookLimitOffsetPagination,BookPageNumberpagination

# Create your views here.


###  list books ---- and add/create
class BookList(ListCreateAPIView):
    permission_classes = (AllowAny, )
    # queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    ### pagination 
    pagination_class = BookPageNumberpagination

    ## user show the user as requested ****
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    #### restframe search
    # books/?search=book&ordeing=title
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'slug']
    
    # books/?q=book
    def get_queryset(self, *args, **kwargs):
        queryset_list = Book.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(description__icontains=query)|
                    Q(slug__icontains=query)
            ).distinct()
        return queryset_list

    


### Book details 
class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    
### Book delete   
class BookDelete(DestroyAPIView):
    ### only admin and update and delete ... 
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = (IsAdminUser, )


### Book update  
### retrive update view gives us pre filled details ... 
class BookUpdate(RetrieveUpdateAPIView):
    ### only admin and update and delete ... 
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = (IsAdminUser, )


#### list all featured books
class FeaturedList(ListAPIView): 
    permission_classes = (AllowAny, )
    ### return a singal/list of objects
    queryset  = Book.objects.filter(featured=True)
    serializer_class = BookDetailSerializer
    pagination_class = None