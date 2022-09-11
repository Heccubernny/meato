from django.contrib import admin
from MainContainer.models import Meat, MeatType, Staff, Store, User

# Register your models here.
admin.site.register((MeatType,Store,User,Meat,Staff))
