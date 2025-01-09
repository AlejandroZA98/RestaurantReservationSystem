from django.db import models
from django.contrib.auth.models import User
from reservation_app.api.models.clients_model import Client
from reservation_app.api.models.tables_model import Table

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.client