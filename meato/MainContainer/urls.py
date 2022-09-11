from django.urls import include, path
from MainContainer.views import (MeatTypeViewSet, MeatViewSet, StaffViewSet,
                                 StoreViewSet, UserViewSet)
from rest_framework import routers

router = routers.DefaultRouter()

router.register('store', StoreViewSet, basename='store')
router.register('meattype', MeatTypeViewSet, basename='meattype')
router.register('meat', MeatViewSet, basename='meat')
router.register('user', UserViewSet, basename='user')
router.register('staff', StaffViewSet, basename='staff')


urlpatterns = [
    path('', include(router.urls)),
]
