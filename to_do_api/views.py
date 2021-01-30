from django.contrib.auth.models import User
from . import serializers, models

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = models.ToDo.objects.all()
    serializer_class = serializers.ToDoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})