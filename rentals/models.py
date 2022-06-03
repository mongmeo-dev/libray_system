from django.db import models, transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from accounts.models import User
from books.models import Book


def calculate_return_date():
    return timezone.now() + timezone.timedelta(days=7)


class BookRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    return_date = models.DateTimeField(default=calculate_return_date)

    def __str__(self):
        return f'{self.pk} {self.user} - {self.book}({self.book_quantity})'

    @classmethod
    @transaction.atomic
    def rental_book(cls, user, serializer):
        if not user.can_rent:
            print(user.can_rent)
            raise ValidationError({'message': '대출 금지 상태입니다.'})

        book = serializer.validated_data['book']
        book.stock -= serializer.validated_data['book_quantity']

        serializer.validated_data['user'] = user

        serializer.save()
        book.save()
        return serializer

    @transaction.atomic
    def return_book(self):
        book = self.book
        book.stock += self.book_quantity
        book.save()

        if self.return_date < timezone.now():
            user = self.user
            penalty_days = timezone.now() - self.return_date
            user.penalty_date = timezone.now() + penalty_days
            user.save()

        self.delete()
