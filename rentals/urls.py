from rest_framework.routers import DefaultRouter

from .views import RentalViewSet

app_name = 'rentals'

router = DefaultRouter()
router.register('', RentalViewSet)

urlpatterns = []
urlpatterns += router.urls
