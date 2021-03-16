from django.urls import path, include
from aluno import views

urlpatterns = [
    path('login/', views.LoginView, name='login_aluno'),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view())
]