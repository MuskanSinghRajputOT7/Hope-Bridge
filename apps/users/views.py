# apps/users/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User, NGO
from .serializers import UserSerializer, RegisterSerializer, NGOSerializer
from .authentication import generate_jwt_token

# ============ YOUR API VIEWS ============
# (Keep all your existing API functions here)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'success': True,
            'message': 'User registered successfully',
            'user_id': user.user_id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(email=email, password=password)
    if user:
        token = generate_jwt_token(user)
        serializer = UserSerializer(user)
        return Response({
            'success': True,
            'token': token,
            'user': serializer.data
        })
    return Response({
        'success': False,
        'message': 'Invalid credentials'
    }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({
            'error': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ngo(request):
    if request.user.role != 'ngo_staff':
        return Response({
            'error': 'Only NGO staff can create NGO profiles'
        }, status=status.HTTP_403_FORBIDDEN)
    
    if NGO.objects.filter(user=request.user).exists():
        return Response({
            'error': 'You already have an NGO profile'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    data = request.data.copy()
    data['user'] = request.user.user_id
    
    serializer = NGOSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'ngo_id': serializer.data['ngo_id'],
            'message': 'NGO registered. Awaiting admin verification.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_ngos(request):
    ngos = NGO.objects.filter(is_verified=True)
    serializer = NGOSerializer(ngos, many=True)
    return Response({
        'count': len(serializer.data),
        'ngos': serializer.data
    })