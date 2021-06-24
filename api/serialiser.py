from django.db.models import fields
from rest_framework import serializers
from base.models import Text
from django.contrib.auth.models import User

class TextSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'text', 'created_at', 'modified_at']


class UserSerialiser(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'password2': {'write_only' : True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password must match'})
        user.set_password(password)
        user.save()

        return user
