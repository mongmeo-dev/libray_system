from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginView, logout_view, UserViewSet, UserRentalView

app_name = 'accounts'

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/rentals/', UserRentalView.as_view(), name='user_rental')
]

urlpatterns += router.urls
