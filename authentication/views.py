from .models import User
#from django.http import JsonResponse
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, ConfirmationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.conf import settings
from datetime import datetime, timedelta
from . import helper


#-------------------------------------------------------- Login ----------------
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        try:
            user = authenticate(request, email=data['email'], password=data['password'])
            login(request, user)
            token = RefreshToken.for_user(user)
            token_response = { "refresh": str(token), "access": str(token.access_token) }
            response = { 'token':token_response , 'user':UserSerializer(user).data }
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response('username or password is incorrect', status=status.HTTP_406_NOT_ACCEPTABLE)

#---------------------------------------------------------- logout -------------
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            return Response('User Logged out successfully', status=status.HTTP_200_OK)
        except Exception as e:
            print('-------------')
            print(e)
            return Response('Error in logout', status=status.HTTP_400_BAD_REQUEST)

#-------------------------------------------------------- Register -------------
class Register(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = serializer.errors)
        user = User.objects.create_user(email=data['email'], password=data['password'])
        login(request, user)
        token = RefreshToken.for_user(user)
        token_response = { "refresh": str(token), "access": str(token.access_token) }
        response = { 'token':token_response , 'user':UserSerializer(user).data }
        return Response(response, status=status.HTTP_200_OK)

#--------------------------------------------------------- Profile -------------
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        profile = User.objects.get(id=request.user.id)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        profile = User.objects.get(id=request.user.id)
        data = request.data
        data['username']=profile.username
        data['password']=profile.password
        serializer = UserSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

#------------------------------------------------------ Activation -------------
class Activation(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        code = helper.random_code()
        profile = User.objects.get(id=self.request.user.id)
        profile.otp = code
        profile.save()
        if helper.send_code(profile, code):
            return Response("Activation code send to {}".format(profile.email) , status=status.HTTP_200_OK)
        else:
            return Response("Error sending email - Please try again!" , status=status.HTTP_400_BAD_REQUEST)

#---------------------------------------------------- Confirmation -------------
class Confirmation(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data = serializer.errors)
        profile = User.objects.get(id=self.request.user.id)
        if data['code'] == str(profile.otp):
            profile.confirmed = True
            profile.save()
            token = RefreshToken.for_user(profile)
            token_response = { "refresh": str(token), "access": str(token.access_token) }
            response = { 'token':token_response , 'user':UserSerializer(profile).data }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response("User not verified", status=status.HTTP_406_NOT_ACCEPTABLE)
