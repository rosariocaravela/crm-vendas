from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Client, Interaction
from .forms import ClientForm, InteractionForm

@login_required
def client_list(request):
    clients = Client.objects.all()
    search = request.GET.get('q', '')
    status = request.GET.get('status', '')

    if search:
        clients = clients.filter(
            Q(name__icontains=search) | 
            Q(email__icontains=search) | 
            Q(company__icontains=search)
        )
    if status:
        clients = clients.filter(status=status)

    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'clients/client_list.html', {
        'page_obj': page_obj,
        'search': search,
        'status': status,
    })

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    interaction_form = InteractionForm()
    return render(request, 'clients/client_detail.html', {
        'client': client,
        'interaction_form': interaction_form
    })

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            messages.success(request, 'Cliente criado com sucesso.')
            return redirect('clients:list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('clients:detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form, 'client': client})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Cliente excluído com sucesso.')
        return redirect('clients:list')
    return redirect('clients:detail', pk=client.pk)

@login_required
def add_interaction(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.client = client
            interaction.created_by = request.user
            interaction.save()
            messages.success(request, 'Interação adicionada com sucesso.')
    return redirect('clients:detail', pk=client.pk)
