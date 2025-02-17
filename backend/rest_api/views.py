from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class APITest(APIView):
    def get(self, request):
        return JsonResponse({"message": "API is working!"})

def custom_error_404(request, exception):
    return JsonResponse({'error': 'Not Found'}, status=404)

def custom_error_500(request):
    return JsonResponse({'error': 'Server Error'}, status=500)

def home(request):
    return render(request, 'home.html')  # Render a standard Django template



