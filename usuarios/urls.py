from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("entrar/", LoginView.as_view(), name="login"),
    path("sair/", LogoutView.as_view(), name="logout"),
    path("cadastro/", views.registration, name="registration"),
]