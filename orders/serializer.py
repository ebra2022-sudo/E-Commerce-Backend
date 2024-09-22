from rest_framework import serializers
from .models import Order, OrderItem


# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # To display user's name or username
    order_items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date', 'total_amount', 'status', 'order_items']
