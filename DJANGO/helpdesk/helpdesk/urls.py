# helpdesk/urls.py

from django.contrib import admin
from django.urls import path, include
from tickets.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('', login_view, name='home'),
]
