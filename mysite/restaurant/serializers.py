from rest_framework import serializers
from .models import Restaurant, Category, MenuItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'description', 'price', 'is_available', 'category', 'category_id']


class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone', 'created_at', 'menu_items']


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ['id', 'restaurant', 'items', 'customer_name', 'customer_phone', 'created_at', 'status']
