from django.contrib import admin
from .models import Client, Interaction

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'status', 'created_at')
    search_fields = ('name', 'email', 'company')
    list_filter = ('status', 'created_at')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('client', 'type', 'created_by', 'created_at')
    list_filter = ('type', 'created_at')
