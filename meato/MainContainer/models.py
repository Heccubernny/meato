from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField

# Choice field
STATES = (
    ('edo','Edo'),('ekiti','Ekiti'),('kogi','Kogi'),('kwara','Kwara'),('lagos','Lagos'),
        ('ogun','Ogun'),('ondo','Ondo'),('osun','Osun'),('oyo','Oyo'),
    )

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    meat_category = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATES, default='lagos')
    country = CountryField(blank_label='(select country)', default='NG')
    total_meat = models.IntegerField()
    total_price = models.IntegerField()
    description = models.TextField()
    store_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['store_date']


class MeatType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Meat(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField()
    meat_type = models.ForeignKey(MeatType, on_delete=models.SET_NULL, null=True)
    meat_size = models.CharField(max_length=200)
    meat_price = models.IntegerField()
    meat_category = models.ForeignKey(Store, verbose_name="Meat Category", related_name= "meat_categories", on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slaughtered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.username


class Staff(models.Model):
    image = models.ImageField(blank=True)
    firstname = models.CharField(max_length=32, null=False)
    lastname = models.CharField(max_length=32, default="")
    stipend = models.CharField(max_length = 10)
    phone_no = models.CharField(max_length = 11, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    state = models.CharField(max_length=200, choices=STATES, default='lagos')
    country = CountryField(blank_label='(select country)', default='NG')

    def __str__(self):
        return self.user.username


# class Debtors(models.Model):
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     amount = models.IntegerField()
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     state = models.CharField(max_length=200, choices=STATES)
#     country = CountryField(blank_label='(select country)')
#     signature = models.ImageField(upload_to='images/signature/', blank=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['date']
