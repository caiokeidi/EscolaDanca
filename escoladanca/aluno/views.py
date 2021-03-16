from django.shortcuts import render
from aluno.serializer import AlunoSerializer
from rest_framework import viewsets
from aluno.models import Aluno
from escola.models import Inscricao
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import json


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer



@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def LoginView(request):
    
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        senha = body['password']
        
        

        return Response({'teste'})
    
    
