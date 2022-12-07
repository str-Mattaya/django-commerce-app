from rest_framework import generics, filters, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters import rest_framework as dfilters
from django.contrib.auth import authenticate, login, logout

from store.filters import CaseInsensitiveOrderingFilter, ClassProductFilter
from store.models import Customer, Product
from store.serializers import *


class LoginPage(TokenObtainPairView):
    serializer_class = LoginTokenSerializer


class RegisterPage(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegistrationSerializer


class CustomerInfo(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'username'


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [dfilters.DjangoFilterBackend, filters.SearchFilter, CaseInsensitiveOrderingFilter]
    filterset_class = ClassProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']
    ordering = ['name']


class ProductInfo(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class OwnerInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Customer.objects.get(username=user.username)


class ListCart(generics.ListAPIView):
    serializer_class = CartItemSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(customer__id=user.id)
