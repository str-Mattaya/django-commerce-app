from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters import rest_framework as dfilters
from django.contrib.auth import authenticate, login, logout

from store.filters import CaseInsensitiveOrderingFilter, ClassProductFilter
from store.models import Customer, Product
from store.serializers import *


class LoginPage(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username and password:
            user = authenticate(self.request, username=username, password=password)
            if user:
                # logout(self.request)
                login(self.request, user)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def customer_logout(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)


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
