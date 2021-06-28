from django.contrib import admin
from django.urls import path
from app.views import create_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/', create_webhook, name='create_webhook'),
]
