from django.contrib import admin

from .models import BookRental


@admin.register(BookRental)
class RentalAdmin(admin.ModelAdmin):
    pass
