from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Dislikes
from .serializers import DislikeSerializer

class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislikes.objects.all()
    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticated]
