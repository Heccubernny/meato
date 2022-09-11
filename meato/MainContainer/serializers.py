# from django_countries.serializers import CountryFieldMixin
from MainContainer.models import Meat, MeatType, Staff, Store, User
from rest_framework import serializers

# class CountrySerializer(CountryFieldMixin, serializers.ModelSerializer):

#     class Meta:
#         model = Store
#         fields = ('__all__')

class StoreSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='get_country_display')

    class Meta:
        model = Store
        fields = ('__all__')

class MeatTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeatType
        fields = ('__all__')

class MeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meat
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')

class StaffSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='get_country_display')

    class Meta:
        model = Staff
        fields = ('__all__')
