from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, RegionViewSet


router = DefaultRouter()

router.register(
    r'cities',
    CityViewSet,
    basename='cities'
)

router.register(
    r'regions',
    RegionViewSet,
    basename='regions'
)


urlpatterns = [
    path('', include(router.urls)),
]