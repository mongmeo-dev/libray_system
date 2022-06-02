from django.db import models
from django.utils import timezone

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
