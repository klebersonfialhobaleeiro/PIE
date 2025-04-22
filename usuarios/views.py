from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada, faça login")
            return redirect('login')
        else:
            messages.error(request, "ERRO")
            return redirect('')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/registration.html', {'registration' : True, 'form': form})