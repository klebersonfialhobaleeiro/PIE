from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Animal
from .forms import AnimalForm

@login_required
def listar_animais(request):
    animais = Animal.objects.all().order_by('-data_resgate')
    return render(request, 'resgatapp/listar_animais.html', {'animais': animais})

@login_required
def cadastrar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.resgatado_por = request.user
            animal.save()
            messages.success(request, "Animal resgatado com sucesso!")
            return redirect('listar_animais')
    else:
        form = AnimalForm()
    return render(request, 'resgatapp/cadastrar_animal.html', {'form': form})

@login_required
def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.resgatado_por != request.user or not request.user.is_superuser:
        messages.error(request, "Você não tem permissão para editar este animal.")
        return redirect('listar_animais')

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal atualizado com sucesso!")
            return redirect('listar_animais')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'resgatapp/editar_animal.html', {'form': form, 'animal': animal})

@login_required
def adotar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        animal.adotado = True
        animal.adotado_por = request.user
        animal.data_adocao = datetime.now()
        animal.save()
        messages.success(request, 'O animal foi adotado com sucesso!')
        return redirect('mural_adocao')

def mural_adocao(request):
    especie_filtro = request.GET.get('especie', None)
    adotado_filtro = request.GET.get('adotado', None)

    animais = Animal.objects.all().order_by('-data_resgate')

    if especie_filtro:
        animais = animais.filter(especie=especie_filtro)
    
    if adotado_filtro:
        animais = animais.filter(adotado=(adotado_filtro == 'sim'))

    return render(request, 'resgatapp/mural_adocao.html',{
        'animais': animais,
        'especies': Animal.TIPO_ANIMAL,
    }
    )
