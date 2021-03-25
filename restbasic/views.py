from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from restbasic import serializers,models

from rest_framework.authentication import TokenAuthentication
from restbasic import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework.authtoken.views import  ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview=[
            'Hello',
            'Is similar to django  view',
            'Mappend manually to URLS'
        ]
        return Response({'message':"Hello",'an_apiview':an_apiview})

    def post(self, request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        return Response({'message':'Hello'})
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello ! {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def retrieve(self,request,pk=None):
        return Response({'http_methhod':'GET'}) 

    def update(self,request,pk=None,*args, **kwargs):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):

    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()

    def perform_create(self,serializer):

        serializer.save(user_profile=self.request.user)