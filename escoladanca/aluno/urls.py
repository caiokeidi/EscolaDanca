from django.urls import path, include
from aluno import views

urlpatterns = [
    path('login/', views.LoginView, name='login_aluno')
]