from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, BookListByTitleView, BookListByAuthorView

app_name = 'books'

router = DefaultRouter()
router.register('', BookViewSet, basename='book')

urlpatterns = [
    path('title/<str:title>/', BookListByTitleView.as_view(), name='book_by_title'),
    path('author/<str:author>/', BookListByAuthorView.as_view(), name='book_by_author'),
]
urlpatterns += router.urls
