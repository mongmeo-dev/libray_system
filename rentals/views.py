from django.db import transaction
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
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
        user = self.request.user
        if not user.can_rent:
            print(user.can_rent)
            raise ValidationError({'message': '대출 금지 상태입니다.'})

        book = serializer.validated_data['book']
        book.stock -= serializer.validated_data['book_quantity']

        serializer.validated_data['user'] = user

        serializer.save()
        book.save()
        return serializer

    def perform_destroy(self, instance):
        instance.return_book()
