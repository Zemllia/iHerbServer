import datetime

from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.compat import coreapi, coreschema
from iHerbServer.api.v1.serializers import UserSerializer, CustomAuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import viewsets, mixins, filters, parsers, renderers
from iHerbServer.models import *


class iHerbServerViewMixin(object):
    serializer_classes = {}
    action = None
    querysets = {}
    queryset = None
    serializer_class = None

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_classes.get('default', self.serializer_class))

    def get_queryset(self):
        return self.querysets.get(self.action, self.querysets.get('default', self.queryset))


class UserCodeLoginView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=False,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
                # remove
                coreapi.Field(
                    name="UUID",
                    required=False,
                    location='form',
                    schema=coreschema.String(
                        title="UUID",
                        description="Valid UUID of device",
                    ),
                ),
                coreapi.Field(
                    name="phone",
                    required=False,
                    location='form',
                    schema=coreschema.String(
                        title="Phone",
                        description="Valid phone number"
                    )
                )
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        """if request.data['UUID'] != user.uuid:
            print(datetime.date.today() - datetime.timedelta(days=7))
            if user.changeDeviceDelay > datetime.date.today() - datetime.timedelta(days=7):
                return Response({'status': 'error', 'message': 'Cant change device'})
            else:
                user.uuid = request.data['UUID']
                user.changeDeviceDelay = datetime.date.today()
                user.save()"""
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserRegisterView(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"message": "success"})


class UserViewSet(iHerbServerViewMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    search_fields = ['email', 'first_name', 'phone']
    filter_backends = (filters.SearchFilter, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
