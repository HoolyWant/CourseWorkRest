from django.contrib.auth import user_logged_in
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import RegisterSerializer, MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserRetrieveApi(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
