from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BookRental


class BookRentalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    return_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BookRental
        fields = ['user', 'book', 'book_quantity', 'created_at', 'return_date']

    def validate(self, attrs):
        if attrs['book'].stock < attrs['book_quantity']:
            raise ValidationError('재고가 부족합니다.')
        return attrs


class BookRentalUpdateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(read_only=True)
    book_quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookRental
        fields = ['user', 'book', 'book_quantity', 'return_date']
