from django.urls import path
from . import views

urlpatterns = [
    path('animais/', views.listar_animais, name='listar_animais'),
    path('animais/cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('animais/editar/<int:animal_id>/', views.editar_animal, name='editar_animal'),
    path('animais/adotar/<int:animal_id>/', views.adotar_animal, name='adotar_animal'),
    path('mural-adocao/', views.mural_adocao, name='mural_adocao'),
]
