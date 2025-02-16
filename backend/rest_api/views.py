from rest_framework.views import APIView
from rest_framework.response import Response

class APITest(APIView):
    def get(self, request):
        data = {"message": "API is working!"}
        return Response(data, content_type="application/json")