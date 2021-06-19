import datetime

from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _
from iHerbServer.models import User


class CustomAuthTokenSerializer(AuthTokenSerializer):
    username = serializers.CharField(label=_("Username"), required=False)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    phone = serializers.CharField(label=_("Phone"), required=False)
    # uuid = serializers.CharField(label=_("UUID"), required=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        phone = attrs.get('phone')
        if phone:
            username = User.objects.filter(phone=int(phone)).first()
            user = authenticate(request=self.context.get('request'), username=str(username), password=password)
            if not user:
                msg = _('Unable to log in with provided credentials')
                raise serializers.ValidationError(msg, code='authorization')
            attrs['user'] = user
            return attrs
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" or "phone" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        print(user.is_superuser)
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone')

    def create(self, validated_data):
        """try:
            is_uuid_exists = User.objects.get(uuid=validated_data['uuid'])
            raise exceptions.NotAuthenticated('Cant register multiply users in one device')
        except Exception as e:
            print(e)"""
        user = User.objects.create_user(**validated_data)
        user.changeDeviceDelay = datetime.date.today()
        user.changeUserInfoDelay = datetime.date.today()
        user.save()
        return user

