from rest_framework import serializers

from store.models import *


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        return Customer.objects.create_user(username=username, password=password, **validated_data)

    class Meta:
        model = Customer
        fields = ['username', 'password', 'name', 'gender', 'phone_number', 'address', 'profile_image']


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['username', 'password']


class CustomerSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)

    class Meta:
        model = Customer
        fields = ['username', 'name', 'gender', 'phone_number', 'address', 'profile_image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'description', 'image']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'customer', 'product', 'amount']
