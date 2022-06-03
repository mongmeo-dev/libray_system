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

    def perform_create(self, serializer):
        return BookRental.rental_book(self.request.user, serializer)

    def perform_destroy(self, instance):
        instance.return_book()
