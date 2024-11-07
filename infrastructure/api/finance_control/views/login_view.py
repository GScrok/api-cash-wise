from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
            
        user = authenticate(username=username, password=password)
            
        if user is not None:
                refresh = RefreshToken.for_user(user)
                
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'id': str(user.id),
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                        }
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'Credenciais inválidas'
            }, status=status.HTTP_401_UNAUTHORIZED)