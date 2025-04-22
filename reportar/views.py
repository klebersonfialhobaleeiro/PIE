from django.shortcuts import get_object_or_404, redirect, render
from .models import Relato
from .forms import RelatoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    return render(request, 'reportar/list.html', {"relatos": Relato.objects.all()})

@login_required
def creat(request):
    if request.method == 'POST':
        form = RelatoForm(request.POST, request.FILES)
        
        if form.is_valid():
            relato = form.save(commit=False)
            relato.usuario = request.user
            relato.save()
            messages.success(request, "Relato enviado com sucesso.")
            return redirect('reports-listar')
        
        for field, errors in form.errors.items():
            if field == "poligono":
                messages.error(request, "Selecione um local no mapa")
            else:
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")

        return redirect('reports-adicionar')

    else:
        form = RelatoForm()
    
    return render(request, 'reportar/add.html', {"form": form, "relatos": Relato.objects.all()})

@login_required
def myreports(request):
    if request.user.is_staff:
        relatos = Relato.objects.all().order_by('-data_relato')
    else:
        relatos = Relato.objects.filter(usuario=request.user).order_by('-data_relato')

    return render(request, 'reportar/myreports.html', {'relatos': relatos})

@login_required
def detail(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)
    pode_editar = request.user == relato.usuario or request.user.is_staff

    return render(request, 'reportar/detail.html', {
        'relato': relato,
        'pode_editar': pode_editar,
        'form': RelatoForm(instance=relato) if pode_editar else None
    })

@login_required
def edit(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)

    if relato.usuario != request.user and not request.user.is_staff:
        messages.error(request, "Você não tem permissão para editar esse relato.")
        return redirect('reports-meus')

    if request.method == 'POST':
        form = RelatoForm(request.POST, request.FILES, instance=relato)
        if form.is_valid():
            form.save()
            messages.success(request, "Relato atualizado com sucesso.")
            return redirect('reports-detalhe', relato_id=relato.id)

@login_required
def delete(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)

    if relato.usuario != request.user and not request.user.is_staff:
        messages.error(request, "Você não tem permissão para excluir esse relato.")
        return redirect('reports-meus')

    if request.method == 'POST':
        relato.delete()
        messages.success(request, "Relato excluído com sucesso.")
        return redirect('reports-meus')