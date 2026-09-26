from django.contrib import admin
from .models import Stage, Deal

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'color']
    list_editable = ['order', 'color']

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'stage', 'value', 'expected_close_date', 'owner']
    list_filter = ['stage', 'client', 'owner']
    search_fields = ['title', 'description', 'client__name']
