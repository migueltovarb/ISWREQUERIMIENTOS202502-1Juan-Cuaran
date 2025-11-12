from django.db import models
from django.utils import timezone

# Create your models here.

class Credentials (models.Model):
    credential_code = models.CharField(max_length=6)
    visitor = models.ForeignKey('visitors.Visitor', on_delete=models.CASCADE)    
    active = models.BooleanField(default=True)
    restricted = models.BooleanField(default=False)
    expiration_date = models.DateTimeField()


    def is_valid (self):
        return (self.active and not self.restricted and self.expiration_date > timezone.now())
    
    