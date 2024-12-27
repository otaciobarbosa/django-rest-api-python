from rest_framework import viewsets
from books.api import serializers
from books.models import Books

class BookViewSet(viewsets.ModelViewSet):  
    serializer_class = serializers.BookSerializer  
    queryset = Books.objects.all()  
