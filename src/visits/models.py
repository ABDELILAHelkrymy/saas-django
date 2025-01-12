from django.db import models

# Create your models here.
class Visit(models.Model):
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.path} - {self.timestamp}'