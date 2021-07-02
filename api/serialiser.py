from django.db.models import fields
from rest_framework import serializers
from base.models import Text
from django.contrib.auth.models import User

class TextSerialiser(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_text')
    class Meta:
        model = Text
        fields = ['id', 'text', 'created_at', 'modified_at', 'username', 'emotion']
        extra_kwargs = {
                'created_at' : {'read_only' : True},
                'modified_at': {'read_only' : True},
                'emotion' : {'read_only' : True}
        }
    def get_username_from_text(self, text):
        username = text.client.username
        return username

class UserSerialiser(serializers.ModelSerializer):
    #password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    #email = serializers.EmailField(max_length=255, min_length=4, write_only=True)
    #username = serializers.CharField(max_length=255, min_length=4, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined', 'last_login', 'is_staff']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'password2': {'write_only' : True}
        }

    """def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password must match'})
        user.set_password(password)
        user.save()

        return user
"""
