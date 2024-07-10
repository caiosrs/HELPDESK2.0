# tickets/models.py

from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    CATEGORY_CHOICES = (
        ('suporte', 'Suporte'),
        ('facilites', 'Facilites'),
        ('rh', 'Recursos Humanos'),
        ('outro', 'Outro'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='suporte')
    anydesk_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField(blank=True, null=True)
    STATUS_CHOICES = (
        ('aberto', 'Aberto'),
        ('respondido', 'Respondido'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return self.title

    @property
    def opened_by(self):
        return self.user.username

    def respond_ticket(self, response):
        self.response = response
        self.status = 'respondido'
        self.save()

    def has_response(self):
        return bool(self.response)

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return f'Settings for {self.user.username}'