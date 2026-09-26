from django.core.management.base import BaseCommand
from pipeline.models import Stage

class Command(BaseCommand):
    help = 'Creates default pipeline stages if none exist'

    def handle(self, *args, **kwargs):
        if Stage.objects.exists():
            self.stdout.write(self.style.WARNING('Stages already exist. Skipping creation.'))
            return

        stages = [
            {'name': 'Prospecto', 'order': 1, 'color': '#3b82f6'},
            {'name': 'Qualificado', 'order': 2, 'color': '#8b5cf6'},
            {'name': 'Proposta', 'order': 3, 'color': '#f59e0b'},
            {'name': 'Negociação', 'order': 4, 'color': '#f97316'},
            {'name': 'Fechado Ganho', 'order': 5, 'color': '#22c55e'},
            {'name': 'Fechado Perdido', 'order': 6, 'color': '#ef4444'},
        ]

        for stage_data in stages:
            Stage.objects.create(**stage_data)
            self.stdout.write(self.style.SUCCESS(f"Created stage: {stage_data['name']}"))
        
        self.stdout.write(self.style.SUCCESS('Successfully created default stages.'))
