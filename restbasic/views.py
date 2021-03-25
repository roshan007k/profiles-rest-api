from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from restbasic import serializers

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




