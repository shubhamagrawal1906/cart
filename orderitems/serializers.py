from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import OrderItem, Order

class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['title', 'quantity', 'price', 'order']

    def validate(self, data):
        title = data["title"]
        quantity = data["quantity"]
        price = data["price"]
        order = data["order"]
        orderitem_obj = OrderItem.objects.filter(order=order)
        if not order.user == self.context['request'].user:
            raise ValidationError("Authenticated user accessing wrong order.")
        elif orderitem_obj.count() >= order.total_order:
            raise ValidationError("All items are already listed.")
        elif quantity < 1:
            raise ValidationError("Atleast one quantity is required.")
        elif price < 0:
            raise ValidationError("Incorrect price.")
        elif OrderItem.objects.filter(order=order).filter(title=title).count() >= 1:
            raise ValidationError(title + " already listed here.")
        return data

    def create(self, validated_data):
        title = validated_data["title"]
        quantity = validated_data["quantity"]
        price = validated_data["price"]
        order = validated_data["order"]
        orderitem_obj = OrderItem(title=title, quantity=quantity, price=price, order=order)
        orderitem_obj.save()
        return validated_data

class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'title', 'quantity', 'price', 'order']
