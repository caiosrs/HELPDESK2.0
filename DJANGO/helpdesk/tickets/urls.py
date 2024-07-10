# tickets/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('new/', views.ticket_create, name='ticket_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket/<int:ticket_id>/responder/', views.ticket_responder, name='ticket_responder'),
    path('ticket/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
    path('settings/', views.user_settings, name='settings'),
]
