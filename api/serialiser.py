##############
#   IMPORT   #
##############

from django.db.models import fields
from rest_framework import serializers
from base.models import Text
from django.contrib.auth.models import User

##############
#    TEXT    #
##############

# Text serialiser
class TextSerialiser(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_text')
    class Meta:
        model = Text
        # Fields that will used for the serialisation
        fields = ['id', 'text', 'created_at', 'modified_at', 'username', 'emotion']
        extra_kwargs = {
            # Restrict those fields to be only readable, and disable updating 
                'created_at' : {'read_only' : True},
                'modified_at': {'read_only' : True},
                'emotion' : {'read_only' : True}
        }
    def get_username_from_text(self, text):
        """
        Return the client username
        """
        username = text.client.username
        return username


##############
#    USER    #
##############

# User Serialiser
class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        # Model => Entity reference
        model = User
        fields = ['id', 'email', 'username', 'date_joined', 'last_login', 'is_staff']
        extra_kwargs = {
            # Restrict those fields tho be only writable, they won't be displayed when the admin request the api
            'password' : {'write_only' : True},
            'password2': {'write_only' : True}
        }