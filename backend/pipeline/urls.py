from django.urls import path
from . import views

app_name = 'pipeline'

urlpatterns = [
    path('', views.board_view, name='board'),
    path('deal/create/', views.deal_create, name='deal_create'),
    path('deal/<int:pk>/edit/', views.deal_edit, name='deal_edit'),
    path('deal/<int:pk>/delete/', views.deal_delete, name='deal_delete'),
    path('deal/update-stage/', views.update_deal_stage, name='update_deal_stage'),
]
