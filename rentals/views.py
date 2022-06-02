from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import BookRental
from .permissions import IsAdminOrOwner
from .serializers import BookRentalSerializer, BookRentalUpdateSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = BookRental.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'update', 'partial_update']:
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [IsAdminOrOwner()]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return BookRentalUpdateSerializer
        return BookRentalSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        book.stock -= serializer.validated_data['book_quantity']
        serializer.validated_data['user'] = self.request.user
        serializer.save()
        book.save()
        return serializer

    @transaction.atomic
    def perform_destroy(self, instance):
        book = instance.book
        book.stock += instance.book_quantity
        book.save()
        instance.delete()
