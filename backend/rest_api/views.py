from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}        
        return Response(data)