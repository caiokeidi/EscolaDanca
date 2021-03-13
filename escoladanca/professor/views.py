from django.shortcuts import render
from rest_framework import viewsets
from professor.models import Professor
from professor.serializer import ProfessorSerializer

class ProfessoresViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
