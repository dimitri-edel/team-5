from django.views.generic.base import View # it's here because this is views.py. Ya might need it
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_api.serializers import MessageSerializer

class HelloWorld(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}
        serializer = MessageSerializer(data)
        return Response(serializer.data)