from rest_framework import serializers
from ..models import Product, ProductOption, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['name']


class ProductOptionSerializer(serializers.ModelSerializer):
    option = OptionSerializer()

    class Meta:
        model = ProductOption
        fields = ["option", "option_value", ]
        # "option_image"

    def create(self, validated_data):
        option_data = validated_data.pop('option')

        option = Option.objects.filter(**option_data)[0]
        if not option:
            option = Option.objects.create(**option_data)

        product = self.context['product_id']
        product_option = ProductOption.objects.create(option=option, product=product, **validated_data)

        return product_option



class AddProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, write_only=True)
    class Meta:
        model = Product
        fields = ["vendor", "name", "brand", "model", "price", "quantity", "made_in", "description",
                  "category","options"]
        # "image",

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        product = Product.objects.create(**validated_data)

        for option_data in options_data:
            product_option_serializer = ProductOptionSerializer(data=option_data, context={'product_id': product})
            if product_option_serializer.is_valid():
                product_option_serializer.save()

        print("hello")
        return product
