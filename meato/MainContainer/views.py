from MainContainer.models import Meat, MeatType, Staff, Store, User
from MainContainer.serializers import (MeatSerializer, MeatTypeSerializer,
                                       StaffSerializer, StoreSerializer,
                                       UserSerializer)
from rest_framework import viewsets

# from rest_framework.permissions import IsAuthenticated


# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = None
    # permission_classes = (IsAuthenticated,)


class MeatTypeViewSet(viewsets.ModelViewSet):
    queryset = MeatType.objects.all()
    serializer_class = MeatTypeSerializer
    # permission_classes = (IsAuthenticated,)


class MeatViewSet(viewsets.ModelViewSet):
    queryset = Meat.objects.all()
    serializer_class = MeatSerializer
    # permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # permission_classes = (IsAuthenticated,)
