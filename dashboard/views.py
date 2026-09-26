from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from datetime import datetime
from dateutil.relativedelta import relativedelta
from clients.models import Client, Interaction
from pipeline.models import Deal, Stage

@login_required
def index(request):
    total_clients = Client.objects.count()
    total_deals = Deal.objects.count()
    total_pipeline_value = Deal.objects.aggregate(total=Sum('value'))['total'] or 0
    
    won_stage = Stage.objects.filter(name='Fechado Ganho').first()
    if won_stage:
        won_deals = Deal.objects.filter(stage=won_stage)
        won_deals_count = won_deals.count()
        won_deals_value = won_deals.aggregate(total=Sum('value'))['total'] or 0
    else:
        won_deals_count = 0
        won_deals_value = 0
        
    conversion_rate = (won_deals_count / total_deals * 100) if total_deals > 0 else 0
    
    stages = Stage.objects.annotate(deal_count=Count('deals'))
    deals_by_stage = [
        {'name': stage.name, 'count': stage.deal_count, 'color': stage.color}
        for stage in stages
    ]
    
    six_months_ago = datetime.now() - relativedelta(months=5)
    monthly_data = (
        Deal.objects.filter(stage__name='Fechado Ganho', created_at__gte=six_months_ago)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(revenue=Sum('value'))
        .order_by('month')
    )
    
    monthly_revenue = [
        {'month': data['month'].strftime('%b %Y'), 'revenue': float(data['revenue'])}
        for data in monthly_data
    ]
    
    recent_activities = Interaction.objects.select_related('client').order_by('-created_at')[:5]
    recent_deals = Deal.objects.select_related('client', 'stage').order_by('-created_at')[:5]
    
    context = {
        'total_clients': total_clients,
        'total_deals': total_deals,
        'total_pipeline_value': total_pipeline_value,
        'won_deals_value': won_deals_value,
        'conversion_rate': conversion_rate,
        'deals_by_stage': deals_by_stage,
        'monthly_revenue': monthly_revenue,
        'recent_activities': recent_activities,
        'recent_deals': recent_deals,
    }
    
    return render(request, 'dashboard/index.html', context)
