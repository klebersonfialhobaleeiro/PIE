from django.urls import path
from . import views

urlpatterns = [
    path("listar/", views.list, name="reports-listar"),
    path("adicionar/", views.creat, name="reports-adicionar"),

    path('meus/', views.myreports, name='reports-meus'),
    path('<int:relato_id>/', views.detail, name='reports-detalhe'),
    path('editar/<int:relato_id>/', views.edit, name='reports-editar'),
    path('deletar/<int:relato_id>/', views.delete, name='reports-deletar'),

]