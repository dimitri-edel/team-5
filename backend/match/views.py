from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Match
from .serializers import MatchSerializer
from .permissions import Matched

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated, Matched]


