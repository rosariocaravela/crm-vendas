from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Stage, Deal
from .forms import DealForm
import json

@login_required
def board_view(request):
    stages = Stage.objects.prefetch_related('deals').all()
    
    overall_total = 0
    stages_data = []
    
    for stage in stages:
        deals = stage.deals.all()
        stage_total = sum(deal.value for deal in deals)
        overall_total += stage_total
        stages_data.append({
            'stage': stage,
            'deals': deals,
            'total_value': stage_total,
            'deal_count': deals.count()
        })
        
    context = {
        'stages_data': stages_data,
        'overall_total': overall_total,
    }
    return render(request, 'pipeline/board.html', context)

@login_required
def deal_create(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save(commit=False)
            deal.owner = request.user
            deal.save()
            messages.success(request, 'Oportunidade criada com sucesso.')
            return redirect('pipeline:board')
    else:
        form = DealForm()
    
    return render(request, 'pipeline/deal_form.html', {'form': form, 'is_edit': False})

@login_required
def deal_edit(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oportunidade atualizada com sucesso.')
            return redirect('pipeline:board')
    else:
        form = DealForm(instance=deal)
        
    return render(request, 'pipeline/deal_form.html', {'form': form, 'is_edit': True, 'deal': deal})

@login_required
@require_POST
def deal_delete(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    deal.delete()
    messages.success(request, 'Oportunidade excluída com sucesso.')
    return redirect('pipeline:board')

@login_required
@require_POST
def update_deal_stage(request):
    try:
        data = json.loads(request.body)
        deal_id = data.get('deal_id')
        new_stage_id = data.get('new_stage_id')
        
        deal = get_object_or_404(Deal, pk=deal_id)
        new_stage = get_object_or_404(Stage, pk=new_stage_id)
        
        deal.stage = new_stage
        deal.save()
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
