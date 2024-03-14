from django.db import models

class UserVisit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.ip_address} - {self.timestamp}'
