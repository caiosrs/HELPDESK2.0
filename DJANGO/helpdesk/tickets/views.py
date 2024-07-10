# tickets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from .models import UserSettings
from .forms import UserSettingsForm
from django.conf import settings
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ticket_list')
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
                return render(request, 'tickets/login.html', {'form': form, 'messages': messages.get_messages(request)})
        else:
            messages.error(request, 'Erro no formulário. Por favor, verifique os dados inseridos.')
    else:
        form = AuthenticationForm()

    return render(request, 'tickets/login.html', {'form': form, 'messages': messages.get_messages(request)})

@login_required
def ticket_list(request):
    user = request.user
    if user.is_staff:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(user=user)

    is_admin = user.is_staff

    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'is_admin': is_admin})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(user=request.user)
    return render(request, 'tickets/ticket_form.html', {'form': form})

@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    
    if request.user.is_staff:
        ticket.delete()
        return redirect('ticket_list')
    else:
        return HttpResponseForbidden("Você não tem permissão para excluir este chamado.")

@login_required
def ticket_responder(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    
    if request.method == 'POST':
        response = request.POST.get('response')
        ticket.response = response
        ticket.status = 'respondido'
        ticket.save()
        return redirect('ticket_list')

    return render(request, 'tickets/ticket_responder_modal.html', {'ticket': ticket})

@login_required
def user_settings(request):
    user = request.user
    try:
        settings = UserSettings.objects.get(user=user)
    except UserSettings.DoesNotExist:
        settings = UserSettings(user=user)
    
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = UserSettingsForm(instance=settings)
    
    return render(request, 'tickets/settings.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
