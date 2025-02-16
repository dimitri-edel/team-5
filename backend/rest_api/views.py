from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class HelloWorld(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}
        return Response(data, content_type="application/json")

def custom_error_404(request, exception):
    return JsonResponse({'error': 'Not Found'}, status=404)

def custom_error_500(request):
    return JsonResponse({'error': 'Server Error'}, status=500)