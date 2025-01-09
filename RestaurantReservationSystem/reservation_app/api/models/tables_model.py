from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    chairs=models.IntegerField()
    table=models.IntegerField()
    disponibility=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.table)