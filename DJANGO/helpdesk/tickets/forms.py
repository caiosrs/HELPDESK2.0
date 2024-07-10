# tickets/forms.py

from django import forms
from .models import Ticket
from .models import UserSettings

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'anydesk_id', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'anydesk_id': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ticket = super().save(commit=False)
        if self.user:
            ticket.user = self.user
        if commit:
            ticket.save()
        return ticket

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['dark_mode']
        labels = {
            'dark_mode': 'Modo Escuro',
        }

class TicketResponseForm(forms.Form):
    response = forms.CharField(widget=forms.Textarea)