# Generated by Django 5.0.6 on 2024-07-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_anydesk_id_ticket_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('suporte', 'Suporte'), ('facilites', 'Facilites'), ('rh', 'Recursos Humanos'), ('outro', 'Outro')], default='suporte', max_length=20),
        ),
    ]
