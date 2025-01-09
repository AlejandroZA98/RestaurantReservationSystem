from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=120)
    email   = models.CharField()
    celphone = models.IntegerField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.name