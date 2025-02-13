from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='MEDIUM')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title