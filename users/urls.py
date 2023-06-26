from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Login",
    description="This endpoint allows you to login and obtain a JWT token pair.",
    tags=["Login"]
)

class LoginView(TokenObtainPairView):
    # como pegar o usuário pelo email enviado
    # caso o campo is_active seja falso mudar para verdadeiro
    pass

urlpatterns = [
    path("users/login/", LoginView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<str:pk>/", views.UserDetailView.as_view()),
]
