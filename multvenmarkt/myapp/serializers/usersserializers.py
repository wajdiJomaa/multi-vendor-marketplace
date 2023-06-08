from django.contrib.auth.models import User
from ..models import Customer , Vendor
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ['user', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user = None

        if user_serializer.is_valid():
            user = user_serializer.save()

        phone = validated_data.get("phone")
        address = user_data.get("address")

        customer = Customer(phone=phone, address=address, user=user)
        customer.save()
        return customer
    
class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vendor
        fields = ['user','description','website', 'phone', 'address','profile_photo']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save()
        description = validated_data.get("description")
        website = validated_data.get("website")
        phone = validated_data.get("phone")
        address = user_data.get("address")
        profile_photo = validated_data.get("profile_photo")

        vendor = Vendor(description = description , website = website ,  phone=phone, address=address, profile_photo = profile_photo , user=user)

        return vendor