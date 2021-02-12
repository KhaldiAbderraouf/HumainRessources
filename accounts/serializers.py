from rest_framework import serializers
from accounts.models import *


# UserRight Serializer
class UserRightSerializer(serializers.ModelSerializer):
    has_access = serializers.SerializerMethodField()

    class Meta:
        model = UserRight
        fields = ('user', 'right', 'has_access')

    def get_has_access(self, object):
        return object.user.has_access(object.right.id)


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    user_rights = UserRightSerializer(many=True)

    class Meta:
        model = BaseUser
        fields = ('id', 'username', 'email', 'full_name', 'user_rights')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = BaseUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
