from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []


class BookListByTitleView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Book.objects.filter(title__icontains=title)


class BookListByAuthorView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author__contains=author)
