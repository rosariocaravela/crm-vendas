from django.db import models
from django.contrib.auth.models import User

class Stage(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    color = models.CharField(max_length=7, default='#6366f1')
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

class Deal(models.Model):
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='deals')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='deals')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deals')
    description = models.TextField(blank=True)
    expected_close_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
        
    def __str__(self):
        return self.title
