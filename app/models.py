from django.db import models


class Webhook(models.Model):
    url = models.CharField(max_length=255)
