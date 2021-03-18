from django.shortcuts import render
from aluno.serializer import AlunoSerializer, UserSerializer, UserSerializerWithToken, CadastroAlunoSerializer
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
from django.http import HttpResponseRedirect
from rest_framework import permissions, status



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
        usuario = body['username']
        senha = body['password']
        
        userFilter = User.objects.filter(username=usuario).exists()
        
        if userFilter:
            try:
                user = auth.authenticate(request, username = usuario, password = senha)
            except:
                user = None
            
            if user is not None:
                auth.login(request, user)
                print(f'Usuário {user} logado')
            else:
                print('Usuário ou senha incorreto')



        return Response({'teste'})
    


class CadastroAluno(APIView):
    
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = CadastroAlunoSerializer(data=request.data)
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # serializer = UserSerializerWithToken(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    print(request.user)
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
