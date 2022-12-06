from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomerManager(BaseUserManager):

    def create_user(self, username, password, **kwargs):
        instance = Customer.objects.create(username=username, **kwargs)
        instance.set_password(password)
        instance.save()
        return instance
    
    def create_superuser(self, username, password, **kwargs):
        instance = self.create_user(username, password, **kwargs)
        instance.is_staff = True
        instance.is_superuser = True
        instance.save()
        return instance


class Customer(AbstractUser):

    GENDER_CHOICES = [
        ('male', 'M'),
        ('female', 'F')
    ]

    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=6, default='', choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=255, default='')
    profile_image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomerManager()


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=1)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(null=True, blank=True)


class CartItem(models.Model):

    CART_CHOICES = [
        ('waiting', 'Wait for Payment'),
        ('pending', 'Pending'),
        ('delivering', 'Delivering'),
        ('completed', 'Completed')
    ]

    status = models.CharField(max_length=10, default='waiting', choices=CART_CHOICES)
    slip = models.FileField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='carts')
    amount = models.IntegerField(default=1)
