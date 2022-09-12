from ipaddress import ip_address
from django.db import models
from django.contrib.auth.models import User


class paragraph (models.Model):
    text = models.TextField()
    user_ip = models.CharField(max_length=999, null=True, blank=True)
    username = models.CharField(max_length=99, null=True, blank=True)

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50]+"..."
        return self.text

