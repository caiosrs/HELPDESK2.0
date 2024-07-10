# tickets/migrations/0004_alter_ticket_user.py

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

def set_default_user(apps, schema_editor):
    Ticket = apps.get_model('tickets', 'Ticket')
    User = apps.get_model('auth', 'User')
    default_user = User.objects.first()  # ou obtenha o superusuário ou outro usuário específico
    for ticket in Ticket.objects.filter(user__isnull=True):
        ticket.user = default_user
        ticket.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_user'),  # ajuste conforme necessário
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(set_default_user),
    ]
