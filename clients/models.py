from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    STATUS_CHOICES = (
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
        ('LEAD', 'Lead'),
    )
    
    name = models.CharField(max_length=200, verbose_name="Nome")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    company = models.CharField(max_length=200, blank=True, verbose_name="Empresa")
    address = models.TextField(blank=True, verbose_name="Endereço")
    notes = models.TextField(blank=True, verbose_name="Observações")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='LEAD', verbose_name="Status")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Criado por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

class Interaction(models.Model):
    TYPE_CHOICES = (
        ('LIGAÇÃO', 'Ligação'),
        ('EMAIL', 'Email'),
        ('REUNIÃO', 'Reunião'),
        ('NOTA', 'Nota'),
    )
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions', verbose_name="Cliente")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='NOTA', verbose_name="Tipo")
    description = models.TextField(verbose_name="Descrição")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Criado por")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Interação"
        verbose_name_plural = "Interações"

    def __str__(self):
        return f"{self.type} - {self.client.name}"
