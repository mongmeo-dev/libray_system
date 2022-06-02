from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .permissions import IsNotAuthenticated, IsAdminOrLoggedInUser
from .serializers import LoginSerializer, UserUpdateSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        elif self.action == 'create':
            return [IsNotAuthenticated()]
        return [IsAdminOrLoggedInUser()]

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response(status=status.HTTP_200_OK)
