from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Order, User
from django.core.mail import send_mail
from django.conf import settings
import uuid

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_order', 'payment_method']

    def validate_total_order(self, value):
        total_order = value
        if total_order < 1:
            raise ValidationError("Atleast one order is required.")
        return value

    def create(self, validated_data):
        total_order = validated_data["total_order"]
        payment_method = validated_data["payment_method"]
        token = uuid.uuid4().hex
        user_obj = User.objects.get(username=self.context['request'].user)
        order_obj = Order(total_order=total_order, payment_method=payment_method, user=user_obj, token=token)
        link = "http://" + str(self.context['request'].META['HTTP_HOST']) + "/order/validate/" + token + "/"
        order_obj.save()
        send_mail('Verify your order', 'To approve your order please click here - '+ link, settings.EMAIL_HOST_USER, [user_obj.email], fail_silently=False)
        return validated_data

class OrderListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    payment_method = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'total_order', 'payment_method', 'status']
    def get_status(self, obj):
        return obj.get_status_display()
    def get_payment_method(self, obj):
        return obj.get_payment_method_display()

class OrderDetailSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    payment_method = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'total_order', 'payment_method', 'status']
    def get_status(self, obj):
        return obj.get_status_display()
    def get_payment_method(self, obj):
        return obj.get_payment_method_display()

class OrderValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['token']

    def validate(self, data):
        token = data["token"]
        order_list = Order.objects.filter(token=token)
        if not order_list:
            raise ValidationError("Incorrect token")
        elif not order_list.first().status == 'NA':
            raise ValidationError("Already Approved")
        else:
            order_list.update(status='A')
            print(order_list)
        return data
