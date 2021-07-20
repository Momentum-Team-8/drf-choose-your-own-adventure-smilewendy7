from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from core.models import Book


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'user',
            'title',
            'slug',
            'author',
            'description',
            'featured',
            'publication_date',
        
        ]

## url
book_detail_url = HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='pk'
    )

### delete url
book_delete_url = HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='pk'
    )
class BookCreateSerializer(serializers.ModelSerializer):
    url= book_detail_url 
    delete_url= book_delete_url 
    
    class Meta:
        model = Book
        fields = [
            'url',
            'delete_url',
            'title',
            'slug',
            'author',
            'description',
            'featured',
            'publication_date',
        
        ]