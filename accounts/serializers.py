from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate_email(self, value):
        email = value
        if User.objects.filter(email=email):
            raise ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_instance = User.objects.get(username=username)
        token = Token.objects.create(user=user_instance)
        validated_data['token'] = token.key
        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        user_obj = None
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            raise ValidationError("Username and password are required")
        user = User.objects.filter(username=username).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("The username is not present")
        if user_obj:
            if not user_obj.check_password(password):
                print(user_obj)
                raise ValidationError("Incorrect credentials.")
        token = Token.objects.get(user=user_obj)
        data["token"] = token.key
        return data

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', "last_name"]
